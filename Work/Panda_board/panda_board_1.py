"""Read the csv file and return the string accordingly."""
import csv

main_menu = [
    "General Information",
    "Execute All Test",
    "Memory test",
    "Ethernet Test",
    "UART Test",
    "SPI Test",
    "I2C Test",
    "USB test",
    "HDMI Test",
    "Test Report",
    "Send test report to host machine",
    "Help",
    "Exit"]

main_menu_dict = {
    "General Information": "",
    "Execute All Test": "",
    "Memory test": "",
    "Ethernet Test": {
        "All Tests": 1,
        "MAC LoopBack": 2,
        "PHY LoopBack": 3,
        "Main Menu": 4,
        "Help": 5,
        "Exit": 6
    },
    "UART Test": {
        "All tests": 1,
        "UART LoopBack test": 2,
        "UART View Current Configuration test": 3,
        "UART Baud Rate test": 4,
        "UART Register Read-Write test": 5,
        "UART Transmit test": 6,
        "UART Receive Echo test": 7,
        "UART Transmit FIFO test": 8,
        "UART Receive FIFO Echo test": 9,
        "UART Special Character detect test": 10,
        "UART Transaction tests": 11,
        "Main Menu": 12,
        "Help": 13,
        "Exit": 14
    },
    "SPI test": "",
    "I2C Test": {
        "All tests": 1,
        "I2C bus scan test": 2,
        "I2C loopback test": 3,
        "I2C serial clock line test": 4,
        "I2C software reset test": 5,
        "Main Menu": 6,
        "Help": 7,
        "Exit": 8
    },
    "USB test": "",
    "HDMI test": "",
    "Test Report": "",
    "Send test report to host machine": "",
    "Help": "",
    "Exit": ""}

with open('sample.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for tests in csvreader:
        test_suit, test_cases, execution_cnt = tests[0], tests[1], tests[2]
        test_cases = test_cases.split(",")
        return_string = [main_menu.index(test_suit) + 1]
        for testcase in test_cases:
            return_string.append(main_menu_dict[test_suit][testcase])
        return_string.append(int(execution_cnt))
        return_string.append(main_menu_dict[test_suit]["Main Menu"])
        print(' '.join(map(str, return_string)))
