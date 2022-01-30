import locale
from operator import contains
import sys
from datetime import date, timedelta


def main(args=None):
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


        if (count.isdigit()== False):
            return
        printLastEntries(count)
        return

    entrydate = date.today()
    if (len(args) > 0 and args[0].endswith(':')):
        entrydate = parseDate(args[0])
        args = args[1:]

    createOrUpdate(entrydate, ' '.join(args))


def createOrUpdate(entrydate, text):
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

def parseDate(dateArgument):
    if (dateArgument == 'today:'):
        return date.today()
    
    if (dateArgument == 'yesterday:'):
        return date.today() - timedelta(days=1)

    return date.fromisoformat(dateArgument[:-1])
    
def printLastEntries(count):
    if (count.isdigit()== False):
        return
    for x in range(0,int(count))[::-1]:
        printEntry(date.today() - timedelta(x))
    print("\033[39m")


def printEntry(date):
    filename = date.strftime("%Y-%m-%d") + ".txt"

    try:
        with open(filename, 'r', encoding="utf-8") as fin:
            print('\033[93m' + fin.read())
    except IOError:
        print('\033[95m' + date.strftime("%A, %d. %B %Y") + " \t--- no entry ---")
        print("\033[97m")


if __name__ == "__main__":
    main()