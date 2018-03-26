"""Return test result consolidated report."""

import argparse
import os
import xlwt
import ntpath


def find_test_name(file_name, ext):
    """Return test name from the given file name."""
    test_name = ntpath.basename(file_name)
    test_name = test_name.split(ext)[0]
    return test_name


def get_test_result(file_name, parse_for_fail):
    """Return result of a file.

    If the string "parse for fail" is present in the file, it will return FAIL,
    else it will return PASS.
    """
    result = ""
    if parse_for_fail in open(file_name).read():
        result = "FAIL"
    else:
        result = "PASS"
    return result


def generate_test_result():
    """Generate excel sheet which has file_name with its result."""
    row = 5
    file_list = []

    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Sheet 1")
    sheet1.write(row - 1, 0, 'Test Name')
    sheet1.write(row - 1, 1, 'Result')

    for path, subdirs, files in os.walk(args.dir):
        for filename in files:
            if args.file_ext in filename:
                file_list.append(os.path.join(path, filename))

    for file_name in file_list:
        test_name = find_test_name(file_name, args.file_ext)
        sheet1.write(row, 0, test_name)
        result = get_test_result(file_name, args.fail_string)
        print test_name, result
        sheet1.write(row, 1, result)
        row = row + 1
    book.save("test_result.xls")


parser = argparse.ArgumentParser(description="Generates Report")
parser.add_argument("-d", "--dir", default="dir", required=True)
parser.add_argument("-e", "--file_ext", default=".OUTPUT")
# parser.add_argument("-o", "--output_format", default="xls")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-f", "--fail_string", default="Failed")
group.add_argument("-file", "--fail_file")
args = parser.parse_args()
generate_test_result()
