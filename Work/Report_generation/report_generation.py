"""Generate a report on the basis of given arguments.

usage: report_generation.py -d DIR -e FILE_EXT -o OUTPUT_FORMAT
                           (-f FAIL_STRING | -file FAIL_FILE)
This script searches "FAIL_STRING" in all files with "FILE_EXT" in all the
folders in "DIR" recursively and generates a excel sheet having its results.

If "FAIL_STRING" is present in the file, it returns FAIL, else returns PASS.
"""

import argparse
import os
import xlwt
import ntpath

"""Fail is a dictionary which store the failure string as its key and list of
tests which failed due to it as its value.This dictionary will be initialised
in "get_fail_strings" function.
"""
fail = {}


def get_list_of_files():
    """Return list of files having "FILE_EXT" along with its path."""
    file_list = []
    for path, subdirs, files in os.walk(args.dir):
        for filename in files:
            if args.file_ext in filename:
                file_list.append(os.path.join(path, filename))
    return file_list


def find_test_name(file_name):
    """Return test name from the given file name.

    This funtion takes complete file name as a input and gets the base name of
    the file.It further removes FILE_EXT to get test name.
    """
    test_name = ntpath.basename(file_name)
    test_name = test_name.split(args.file_ext)[0]
    return test_name


def test_result(file_name, parse_for_fail):
    """Return result for "parse_for_fail".

    If the string "parse for fail" is present in the file, it will return FAIL,
    else it will return PASS.
    """
    result = ""
    if parse_for_fail in open(file_name).read():
        result = "FAIL"
    else:
        result = "PASS"
    return result


def failstring_from_file():
    """Return failure strings from FAIL_FILE.

    FAIL_FILE consists of multiple failure strings.This funtion returns a list
    of all failure strings in the file
    """
    failstring = [line.strip("\n")
                  for line in open(args.fail_file)
                  if line.strip("\n") != ""
                  ]
    return failstring


def get_test_results(failstrings, file_name):
    """Return result for multiple fail strings written in file.

    If the strings are present in the input file, it will return FAIL,
    else it will return PASS.
    This funtion also initialises the dictionary "fail" which store the failure
    string as its key and list of tests which failed due to it as its value.
    """
    result_all = []
    result = ""
    for f_str in failstrings:
        result = test_result(file_name, f_str)
        if result == "FAIL":
            fail[f_str].append(find_test_name(file_name))
        result_all.append(result)
    return result_all


def get_fail_strings():
    """Return failure strings."""
    try:
        failstrings = failstring_from_file()
    except:
        failstrings = [args.fail_string]
    for fail_str in failstrings:
        fail[fail_str] = []
    return failstrings


def get_result(file_name, failstrings):
    """Return test_name and its result.

    When the FAIL_FILE is given as an argument, "get_test_results" returns list
    of PASS and FAIL.
    Result is considered as FAIL even if a single entry in the list is FAIL.
    """
    test_name = find_test_name(file_name)
    result = get_test_results(failstrings, file_name)
    if "FAIL" in result:
        result = "FAIL"
    else:
        result = "PASS"
    return test_name, result


def generate_failure_report(book):
    """Generate failure report in second tab if OUTPUT_FORMAT is .xls.

    Second sheet has two columns.First column has Failure string and second
    consists of tests failed due to them.
    """
    row = 1
    sheet2 = book.add_sheet("Failure Report")
    sheet2.write(row - 1, 0, 'Fail String')
    sheet2.write(row - 1, 1, 'Test Name')
    for (fail_string, test_name) in fail.items():
        sheet2.write(row, 0, fail_string)
        for tests in test_name:
            sheet2.write(row, 1, tests)
            row = row + 1
    book.save("test_result.xls")


def generate_xls_test_result():
    """Generate excel sheet which has test_name with its result."""
    row = 1
    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Result")
    sheet1.write(row - 1, 0, 'Test Name')
    sheet1.write(row - 1, 1, 'Result')

    file_list = get_list_of_files()
    failstrings = get_fail_strings()

    for file_name in file_list:
        test_name, result = get_result(file_name, failstrings)
        sheet1.write(row, 0, test_name)
        sheet1.write(row, 1, result)
        row = row + 1
    book.save("test_result.xls")
    generate_failure_report(book)


def generate_csv_test_result():
    """Generate csv file which has test_name with its result."""
    file = open("test_result.csv", "w+")
    file.write("test_name" + "," + "Result" + "," + "\n")
    file_list = get_list_of_files()
    failstrings = get_fail_strings()
    for file_name in file_list:
        test_name, result = get_result(file_name, failstrings)
        file.write(test_name)
        file.write(", ")
        file.write(result)
        file.write(", ")
        file.write("\n")
    file.close()


def generate_txt_test_result():
    """Generate txt file which has test_name with its result."""
    file = open("test_result.txt", "w+")
    file_list = get_list_of_files()
    failstrings = get_fail_strings()
    for file_name in file_list:
        test_name, result = get_result(file_name, failstrings)
        file.write(test_name + " " + result)
        file.write("\n")
    file.close()

parser = argparse.ArgumentParser(description="Generates Report")
parser.add_argument("-d", "--dir", default="dir", required=True)
parser.add_argument("-e", "--file_ext", default=".OUTPUT")
parser.add_argument("-o", "--output_format", default="xls")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-f", "--fail_string")
group.add_argument("-file", "--fail_file")
args = parser.parse_args()
if args.output_format == "xls":
    generate_xls_test_result()
elif args.output_format == "csv":
    generate_csv_test_result()
elif args.output_format == "txt":
    generate_txt_test_result()
