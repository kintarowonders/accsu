import csv, sys, command

def parseRow(row):
	s = row.split('=', 1)
	cmd = s[0]
	oper = s[1]
	command(cmd, oper)


def readFile(filename):
	with open(filename, newline='') as f:
		reader = csv.reader(f)
		for row in reader:
			parseRow(row)
