"""
This module contains the main functionality for a journal application. 

It provides a command-line interface for creating and updating journal entries. 
Entries can be created for the current date or for a specified date. 
The module also supports viewing the last 'n' entries.

Functions:
    main(args=None): The main entry point for the journal application.
    create_or_update(entrydate, text): Creates or updates a journal entry.
"""
import locale
import sys
from datetime import date, timedelta

def main(args=None):
    """
    This function is the main entry point for the journal application. It takes an optional list of arguments
    and processes them accordingly. If no arguments are provided, it prints a message and returns. If the first
    argument starts with a hyphen, it expects a count to follow and prints the last entries from the journal.
    If the first argument ends with a colon, it expects a date to follow and creates or updates an entry for that date.
    Otherwise, it creates or updates an entry for today's date with the provided arguments.
    """
    locale.setlocale(locale.LC_ALL, "")
    if args is None:
        args = sys.argv[1:]

    if (len(args) == 0):
        print("nothing done")
        return

    if (len(args) > 0 and args[0].startswith('-')):
        count = "10"
        if (args[0] == '-n'):
            count = args[1]
        else:
            count = args[0][1:]


        if (not count.isdigit()):
            return
        print_last_entries(count)
        return

    entrydate = date.today()
    if (len(args) > 0 and args[0].endswith(':')):
        entrydate = parse_date(args[0])
        args = args[1:]

    create_or_udate(entrydate, ' '.join(args))


def create_or_udate(entrydate, text):
    """
    Creates a new file or updates an existing file with the given text for the given entry date.

    Args:
    entrydate (datetime): The date of the journal entry.
    text (str): The text to be added to the journal entry.

    Returns:
    None
    """
    filename = entrydate.strftime("%Y-%m-%d") + ".txt"
    file1 = open(filename,"a",  encoding="utf-8")
    current_size = file1.tell()
    if(current_size == 0):
        file1.write(entrydate.strftime("%A, %d. %B %Y") + str('\n'))
    file1.write(str(text) + str('\n'))
    file1.close()
    if(current_size == 0):
        print("[new file created]")
    else:
        print("[new text appended]")



def parse_date(date_argument):
    """
    Parses a date argument and returns a corresponding date object.

    Args:
        dateArgument (str): A string representing a date. Can be in the format 'YYYY-MM-DD' or 'today:' or 'yesterday:'.

    Returns:
        date: A date object corresponding to the input date string.
    """
    if (date_argument == 'today:'):
        return date.today()
    
    if (date_argument == 'yesterday:'):
        return date.today() - timedelta(days=1)

    return date.fromisoformat(date_argument[:-1])
    


def print_last_entries(count):
    """
    Prints the last `count` number of entries in the journal.

    Args:
        count (int): The number of entries to print.

    Returns:
        None
    """
    if (not count.isdigit()):
        return
    for x in range(0,int(count))[::-1]:
        print_entry(date.today() - timedelta(x))
    print("\033[39m")


def print_entry(date_value):
    """
    Prints the contents of a journal entry for the given date.

    Args:
        date_value (datetime.date): The date of the journal entry to print.

    Returns:
        None
    """
    filename = date_value.strftime("%Y-%m-%d") + ".txt"

    try:
        with open(filename, 'r', encoding="utf-8") as fin:
            print('\033[93m' + fin.read())
    except IOError:
        print('\033[95m' + date_value.strftime("%A, %d. %B %Y") + " \t--- no entry ---")
        print("\033[97m")


if __name__ == "__main__":
    main()
