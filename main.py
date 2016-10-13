# Name: Kyle Fritz
# File: main.py
# Date Created: 10/11/16
# Description: Algorithms Project 1, 

import sys # for getting input file

def main():
	filename = sys.argv[-1]
	openedFile = open(filename)

	peopleList = list(openedFile)
	print(peopleList)
	return
main()
