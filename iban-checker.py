
import argparse
import os
import schwifty

def setupArgParser():

	parser = argparse.ArgumentParser()	
	parser.add_argument('iban_file', help='a text file containing the IBANs to check')
	parser.add_argument('--noop', default=False, action='store_true', help='Do nothing, just print configuration and exit')
	return parser


def validateArgument(iban_file):

	if not os.path.isfile(iban_file):
		print('[error]: file not found: {0}'.format(iban_file))
		exit()


def readIBANsFromFile(iban_file):
	
	# https://stackoverflow.com/questions/3277503/in-python-how-do-i-read-a-file-line-by-line-into-a-list
	file = open(iban_file, 'r')
	lines = [line.rstrip('\n') for line in file]
	return lines


if __name__ == '__main__':

	# command-line options
	parser = setupArgParser()
	args = parser.parse_args()

	iban_file = args.iban_file	
	noop = args.noop
	
	validateArgument(iban_file)

	# exit if noop
	if noop:
		print('noop. Exiting.')
		exit()	

	# check IBAN
	# https://pypi.org/project/schwifty/
	iban_list = readIBANsFromFile(iban_file)
	for i in iban_list:
		try:
			iban = schwifty.IBAN(i)
			print('{0}: \tOK (BIC={1})'.format(i, iban.bic))
		except ValueError as err:
			print('{0}: \t{1}'.format(i, err))

