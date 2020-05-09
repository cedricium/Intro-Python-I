"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import date


def print_usage_and_exit(error=''):
    if error != '':
        print('[error] %s\n' % error)

    usage_msg = '[USAGE]\n'
    usage_msg += '    14_cal.py [month | [year]]\n\n'

    usage_msg += '[DESCRIPTION]\n'
    usage_msg += '    Print a calendar for the given month if no arguments given, '
    usage_msg += 'else print the month\n    for the given month and year.\n\n'

    usage_msg += '[ARGUMENTS]\n'
    usage_msg += '\tmonth\t\tthe month you wish to have printed\n'
    usage_msg += '\tyear\t\tthe given year in which to print the month you'

    print(usage_msg)
    exit(1)


def print_calendar(month=date.today().month, year=date.today().year):
    calendar.prmonth(int(year), int(month))


def parse_args():
    num_args = len(sys.argv)
    if num_args > 3:
        num_extra_args = num_args - 3
        print_usage_and_exit(
            error='14_cal.py expects AT MOST 2 arguments, but you provided %d extra args!' % num_extra_args)

    if num_args == 1:
        print_calendar()
    elif num_args == 2:
        print_calendar(sys.argv[1])
    else:
        print_calendar(*sys.argv[1:])


if __name__ == "__main__":
    parse_args()
