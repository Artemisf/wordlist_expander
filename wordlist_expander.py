# This application grabs an existing wordlist and adds whatever you wanna add
# Just type python3 wordlist_expander.py <your path to existing  wordlist> <path/to/your/new/wordlist.txt> <what you want to add>
#!/usr/bin/python
import sys, getopt, re
print('\n\n\n')
print('################################################################################################################################')
print('4r73m15 presents:')
print('wordlist expander v0.0.1')
print('Use: python3 wordlist_expander.py <your path to existing  wordlist> <path/to/your/new/wordlist.txt> <what you want to add>')
print('################################################################################################################################')

#Just for debugging purposes, the number of arguments
number_of_arguments = len(sys.argv)

if number_of_arguments < 5:
#the original argument as a string. First argument is always wordlist_expander.py
	argument_list = str(sys.argv)

#The string looks originally like this ['argument1', 'argument2', 'argument3', 'argument4']
#So we remove all chars that we dont need.
	argument_list = argument_list.replace("[", "")
	argument_list = argument_list.replace("]", "")
	argument_list = argument_list.replace(" ", "")
	argument_list = argument_list.replace("'", "")

#Now we convert the string into an array. We use the comma to separate the words
	inputlist = argument_list.split(",")

#inputfile variable is position 1 from the array
	inputfile = inputlist[1]

#outputfile  variable is position 2 from the array
	outputfile = inputlist[2]

#the content we want to add is position 3 from the array
	addcontent = inputlist[3]



	print('\ninputfile:')
	print(inputfile)
	print('\n\n')

	print('\noutputfile:')
	print(outputfile)
	print('\n\n')

	print('Attachment:')
	print(addcontent)
	print('\n\n')

#open the inputfile to read it 
	existing_file = open(inputfile, 'rt')
	new_file = open(outputfile, 'wt')

	counter = 0
#for reading line by line
	for line in existing_file:
		new_line = line  + addcontent
		new_line = new_line.replace("\n", "")
		new_line = new_line + ('\n')
		new_file.write(new_line)
		counter = counter + 1

#close inputfile
	existing_file.close()
	new_file.close()
	counter = str(counter)
	success = counter + ' lines updated!'
	print(success)
else:
	print('Too many puppies')


