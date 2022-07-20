#python code calling upon a csv file

import csv
with open('hello.csv', newline = '') as csvfile:
	reader = csv.reader(csvfile, delimiter = ',', quotechar = '/')
	for row in reader:
		#print(row)
		print(f'\t{row[0]} is the key and {row[1]} is they value')
