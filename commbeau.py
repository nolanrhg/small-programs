#**********************************************************************
#                                                                    **
# Title: commbeau.py                                                 **
#                                                                    **
# Author: nolanHg                                                    **
#                                                                    **
# Purpose: Makes source code comments look better.                   **
#                                                                    **
# Date: 03/18/2019                                                   **
#                                                                    **
# Created with ahcomm.py                                             **
#                                                                    **
#**********************************************************************


#########
# Imports
#########
import sys


##################################
# Ensure program is used correctly
##################################
if (len(sys.argv) < 2):
	print("\nUsage: python3 commbeau.py <name of file>\n")
	exit()


#########################################
# Get the name of the file to be modified
#########################################
fname = sys.argv[1]


##################
# Read source code
##################
f = open(fname, "r")
code = f.read()
f.close()

lines = code.split("\n")


###################
# Beautify comments
###################
f = open(fname, "w")
for k in range(0, len(lines)):
	l = len(lines[k])
	if (l != 0 and lines[k][-1] != "*" and lines[k][0] == "#"):
			str = "\n" + l * "#" + "\n" + lines[k] + "\n" + l * "#" + "\n" # Create better-looking comment
			f.write(str)
	else:
		f.write(lines[k] + "\n") # Do not modify lines that aren't comments


#################
# Close the file	
#################
f.close()	
