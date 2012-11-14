#!/usr/bin/env python

def deny(name):
	if name=="jordan":
		print "You do not have access!"
	else:
		print "You have access."

def main():
	name = raw_input("Enter your name: ")
	print ("Hello, " + name)
	deny(name)

if __name__=="__main__":
	main()
