from sys import argv

# imports argument values from the command line.
script, filename = argv

# opens $filename and stores the value in variable "txt"
txt = open(filename)

# Calls the read() function on txt with no parameters
print "Here's your file %r:" % filename
print txt.read()

## The following does the same thing, for a different file submitted through user input.  I just used the same ex15_sample.txt file again when running ex15.py.'''

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
