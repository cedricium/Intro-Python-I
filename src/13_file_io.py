"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

from pathlib import Path
current_directory = Path(__file__).resolve().parent

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
with open('%s/foo.txt' % current_directory) as f:
    lines = f.readlines()
    print(*(line for line in lines))

f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

lines = [
    'This is the first line,\n',
    'and this is the second line.\n',
    'Finally, this is the third line!',
]

with open('%s/boo.txt' % current_directory, 'w') as f:
    f.writelines(lines)

f.close()
