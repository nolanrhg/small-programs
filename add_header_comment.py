#**********************************************************************
#                                                                    **
# Title: add_header_comment.py                                       **
#                                                                    **
# Author: nolanrhg                                                   **
#                                                                    **
# Purpose: Creates a header comment for any source code              **
#          file.                                                     **
#                                                                    **
# Date: 07/07/2020                                                   **
#                                                                    **
# Created with add_header_comment.py                                 **
#                                                                    **
#**********************************************************************

# Imports
import sys

###########################################
## Constants
###########################################
H_WIDTH = 71 # width of the header
P_LINE_WIDTH = 50 # purpose line width
GAP = 10 # space before text of next line of
	 # purpose string


###########################################
## Variables
###########################################
pidx = 0 # index for purpose string

###########################################
## Ensure program is used properly
###########################################
if (len(sys.argv) < 2):
	print("\nUsage: python3 add_header_comment.py <name of file>\n")
	exit()


###########################################
## Get the file name and extension from the
## command line
###########################################
fname = sys.argv[1]
title, ext = fname.split(".")


###########################################
## Get the information the user wants to
## put in the header
###########################################
author = input("Enter author of file: ")
purpose = input("Enter purpose of file: ")
date = input("Enter the version date of file: ")


###########################################
## Read the code from the file into a
## variable: it will be rewritten to the 
## input file once the header is written
###########################################
f = open(fname, "r")
code = f.read()
f.close()


###########################################
## Reopen the target file for writing
###########################################
f = open(fname, "w")


###########################################
## Determine what language the code is in
## so that the correct commenting symbol
## can be used
###########################################
if (ext == "m"): ## MATLAB file 

	csymb = "%" # matlab comment symbol

elif (ext == "c" or ext == "cpp" or ext == "java"): ## C, C++, or Java file

	csymb = "//" # c-style comment symbol

elif (ext == "py" or ext == "r"): ## Python or R file

	csymb = "#" # python and R comment symbol


###########################################
## Write header comment to the file
###########################################
f.write(csymb + (H_WIDTH - 1) * '*' + '\n') # top line
f.write(csymb + (H_WIDTH - 3) * ' ' + "**\n") # 'blank' line

title_str = csymb + " Title: " + title + "." + ext # title line
f.write(title_str + (H_WIDTH - len(title_str) - 2) * ' ' + "**\n")
f.write(csymb + (H_WIDTH - 3) * ' ' + "**\n")

author_str =  csymb + " Author: " + author # author line
f.write(author_str + (H_WIDTH - len(author_str) - 2) * ' ' + "**\n")
f.write(csymb + (H_WIDTH - 3) * ' ' + "**\n")

## Break purpose string into multiple
## lines if necessary 
purpose_words = purpose.split(" ")
temp_str = ""
purpose_str = csymb + " Purpose: "
first = True
incomplete = True
while (incomplete):

	if (pidx < len(purpose_words) and len(temp_str + purpose_words[pidx]) < P_LINE_WIDTH):

		temp_str += purpose_words[pidx] + " "
		pidx += 1
	else:   
		purpose_str += ("" if first else csymb + GAP * ' ') + temp_str + \
			       (H_WIDTH - (GAP + 3 + len(temp_str))) * ' ' + \
			       "**\n"
		temp_str = "" # empty the temp string
		if (pidx == len(purpose_words)):
			incomplete = False
		first = False

f.write(purpose_str)
f.write(csymb + (H_WIDTH - 3) * ' ' + "**\n")

date_str = csymb + " Date: " + date # date line
f.write(date_str + (H_WIDTH - len(date_str) - 2) * ' ' + "**\n")
f.write(csymb + (H_WIDTH - 3) * ' ' + "**\n")

cr_str = csymb + " Created with add_header_comment.py "
f.write(cr_str + (H_WIDTH - len(cr_str) - 2) * ' ' + "**\n")
f.write(csymb + (H_WIDTH - 3) * ' ' + "**\n")

f.write(csymb + (H_WIDTH - 1) * '*' + '\n\n')


###########################################
## Write the source code back into the file
## and close the file
###########################################
f.write(code)
f.close()
