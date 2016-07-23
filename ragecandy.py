#!/bin/python
import sys

row = "==========================\n"
print "%sRage Candy\n  Save Exporter for Pokemon Stadium 2\n  by vgmoose\n%s" % (row, row)

path = None

if len(sys.argv) > 1:
    path = sys.argv[1]

# prompt if no file was specified
path = path or raw_input("Enter path to .srm save file: ")

data = open(path, "r+b").read()

print "Loaded %s" % path

print "Currently only data can be exported from \"Anything goes 1-100\""
teams = ord(data[0x00028203])

if teams == 0:
    print "There are no registered Pokemon"
    print "Make sure the registered team is under Anything goes. You can file a bug report or feature request at github.com/vgmoose/ragecandy"
    exit()
else:
    print "Found %s registered team%s!" % (teams, "" if teams==1 else "s")

print "Currently only the first Pokemon is supported"
start = 0x00028210
end = start + 60

poke = list(data[start:end])
# convert this format to a standard one
print ""
print "Before: ", " ".join(["%02x" % ord(x) for x in poke])

for x in range(0, len(poke), 4):
    # swap the two words, and the two bytes with those words
    temp0 = poke[x+2]
    temp1 = poke[x+3]
    poke[x+2] = poke[x+1]
    poke[x+3] = poke[x+0]
    poke[x+0] = temp1
    poke[x+1] = temp0

print " After: ", " ".join(["%02x" % ord(x) for x in poke])

print "\nCopy and paste the \"After\" array into the save file on your gen 2 gbc game"
print "\nThank you for using ragecandy"
