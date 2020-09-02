# Leslie Daniela Sosa
# CS 4375

import sys      # system-specific / command line arguments
import re       # regular expression tools
import os       # to check for file existence

# checks if arguments are correct
if len(sys.argv) != 3:
    print("Correct usage: wordCount.py (input file) (output file)")
    exit()

    # initialize file variables, set sys arguments
    inputFile = (sys.argv[1], 'r')        # Read input file
    outputFile = (sys.argv[2], 'w')       # Write output file

# checks if input text file exists
if not os.path.exists(""):
    print("Text file input %s does NOT exist... Exiting" % inputFile)
    exit()

# holds words from text file
word_count = {}

# loop to scan text file
for data in inputFile:

    # case sensitive arguments A-Z/a-z
    for words in re.split('[^a-zA-Z]', data):
        words = words.lower()

        # add words to word_count
        for words in word_count:
            word_count[words] += 1

        # don't count if word doesn't meet criteria
        else:
            if words != "":
                word_count = 1

# close input file
inputFile.close()

# final_count will hold sorted word list
final_count = sorted(word_count.items())

# final list of words are written in output file and printed
for words in final_count:
    outputFile.write(data[0] + "" + str(data[1]) + '\n')




