from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)

# we could do this on one line, how?
#in_file = open(from_file)
#ndata = in_file.read()

indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exisr? %r" % exists(to_file)