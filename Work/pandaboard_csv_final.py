"""Read the csv file and return the str accordingly.

str will have a no. corresponding to the following in the format given below:
testsuite test_cases execution_cnt "Main_menu"_in_testsuite
"""

import csv


"""main_menu is the list with all test_suit name.

mainmenudict is a nested dictionary which consists of testcases corresponding
to that test_suit
"""

main_menu = [
    "General Information",
    "Execute All Test",
    "Memory Test",
    "Ethernet Test",
    "UART Test",
    "SPI Test",
    "I2C Test",
    "USB Test",
    "HDMI Test",
    "Test Report",
    "Send test report to host machine",
    "Help",
    "Exit"]

mainmenudict = {
    "General Information": "",
    "Execute All Test": "",
    "Memory Test": "",
    "Ethernet Test": {
        "All Tests": 1,
        "MAC LoopBack": 2,
        "PHY LoopBack": 3,
        "Main Menu": 4,
        "Help": 5,
        "Exit": 6
    },
    "UART Test": {
        "All Tests": 1,
        "UART LoopBack Test": 2,
        "UART View Current Configuration Test": 3,
        "UART Baud Rate Test": 4,
        "UART Register Read-Write Test": 5,
        "UART Transmit Test": 6,
        "UART Receive Echo Test": 7,
        "UART Transmit FIFO Test": 8,
        "UART Receive FIFO Echo Test": 9,
        "UART Special Character detect Test": 10,
        "UART Transaction Tests": 11,
        "Main Menu": 12,
        "Help": 13,
        "Exit": 14
    },
    "SPI Test": "",
    "I2C Test": {
        "All Tests": 1,
        "I2C bus scan Test": 2,
        "I2C loopback Test": 3,
        "I2C serial clock line Test": 4,
        "I2C software reset Test": 5,
        "Main Menu": 6,
        "Help": 7,
        "Exit": 8
    },
    "USB Test": "",
    "HDMI Test": "",
    "Test Report": "",
    "Send test report to host machine": "",
    "Help": "",
    "Exit": ""}

with open('sample_1.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for Tests in csvreader:
        """
        1st coloumn of CSV consists of Test Suite.
        2nd coloumn consists of Test cases.
        3rd coloumn consists of execution count.
        """
        Test_suite, Test_cases, execution_cnt = Tests[0], Tests[1], Tests[2]
        Test_cases = Test_cases.split(",")

        try:
            return_string = [main_menu.index(Test_suite) + 1]
        except:
            """ This handles
            1. Case sensitive search of test-suite in main_menu list.
            2. Invalid test_suite entries in CSV
            """
            try:
                Test_suite_1 = Test_suite.lower()
                main_menu_1 = [x.lower() for x in main_menu]
                return_string = [main_menu_1.index(Test_suite_1) + 1]
            except:
                print Test_suite, "is invalid entry..."
                continue

        for Testcase in Test_cases:
            """It either try to find the testcase in the Test_suite as provided
            in CSV or it get the correct test_suite name from the main_menu
            with the help of return string recieved from above block.
            """
            try:
                return_string.append(mainmenudict[Test_suite][Testcase])
            except KeyError as ke:
                try:
                    Test_suite = main_menu[return_string[0] - 1]
                    return_string.append(mainmenudict[Test_suite][Testcase])
                except:
                    """One more reason when above block can raise execption is
                    when testcase search is case sensitive.It is handled in
                    this block.
                    """
                    try:
                        temp = [(x.lower(), y)
                                for (x, y) in mainmenudict[Test_suite].items()
                                if x.lower() == Testcase.lower()
                                ]
                        return_string.append(temp[0][1])
                    except Exception as e:
                        """If Testcase is invalid it will print the error and
                        move forward.
                        """
                        print e
        try:
            return_string.append(int(execution_cnt))
            return_string.append(mainmenudict[Test_suite]["Main Menu"])
            print(' '.join(map(str, return_string)))
        except Exception as e:
            print e
