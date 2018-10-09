#!/usr/bin/env python3
#Python exceptions let you deal with unexpected results

try:
	print(a)	#this will throw an exception since a is not defined (and not a string on its own)
except:
	print("a is not defined!")
	
#there are specific errors to help with this class
try:
	print(a)		#a is not defined, throws exception
except NameError:
	print("a is still not defined!")
except:
	print("Something else went wrong.")
	
#this will break our program because a is not defined
print(a)