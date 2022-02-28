# jrnlfit

This a simple script, that creates a textfile for each day

The usage is similar to the https://jrnl.sh/ tool.

## Usage:
start the script in the folder that contains the text files.
create a batch file that does that for you, for example jrnlfit.bat
Than you could use just 
`jrnlfit -10`

`jrnlfit -> python journal.py`

## Show the last 10 journal entries
`jrnlfit -10`


## Create or update the entry of today or yesterday
The script checks if a text file for the entry existis in the working folder. Then either creates the entry or appends the new text to that existing file.

`jrnlfit today: This day was a very good day.`

`jrnlfit yesterday: Yesterday was very interesting day`

## Create or update the entry of a random day
`jrnlfit 2019-12-04: I have no additional information about this day`


## Delete the entry of a day
just do it by yourself - delete the file - in the folder the the entries. Each day has a its own file with the name:
`2019-12-04.txt`

## Change the contents of an existing entry
just do it by yourself - edit with your text editor - in the folder the the entries. Each day has a its own file with the name:
`2019-12-04.txt`
