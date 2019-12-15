import re
import os
import usaddress

DEBUG = False
SRCDIR='./4_text'
printHeaders=True

# Make it easy to turn off the prints
def debug(*args, **kwargs):
	if DEBUG:
		print(*args, **kwargs)

def processMemory(lines):
	data = "\n".join(lines)
	telMatch = re.search(r'^Tel:\s+(.+)$', data, re.MULTILINE)
	typeMatch = re.search(r'^Type:\s+(.+)$', data, re.MULTILINE)
	return {
		"name"    : lines[0].rstrip(),
		"address" : lines[1].rstrip(),
		"contact" : telMatch.group(1).rstrip() if telMatch else "",
		"type"    : typeMatch.group(1).rstrip() if typeMatch else "",
	}

def processOCR(filename):
	output = []
	with open(filename) as file:
		debug (f'\n\nOPENING {filename}')
		linenum = 0

		memory = []
		record = False
		data = {}
		for line in file:
			l=line.rstrip()

			# skip blank lines
			if re.match(r'^\s+$', line):
				continue

			# Test if line starts with Tel and capture remainder of line
			telMatch = re.search(r'^Tel:\s+(.+)$', l)
			if telMatch:
				if record:
					# if we are already recording, we have reached the end of a record
					output.append(data)
					data = {}
				else:
					# first time through
					record = True
				data['name'] = memory[0]
				data['address'] = memory[1]
				data['tel'] = telMatch.group(1)

				# print("--- ", memory)
				# memory = []
			else:
				if len(memory) >= 2:
					memory.pop(0)
				memory.append(l)

			# Test if line starts with contact and capture remainder of line
			contactMatch = re.search(r'^Contact:\s+(.+)$', l)
			if contactMatch:
				# if 'contact' not in data:
				# 	data['contact'] = []
				data['contact']= contactMatch.group(1)

			emailMatch = re.search(r'^Email:\s+(.+)$', l)
			if emailMatch:
				# if 'email' not in data:
				# 	data['email'] = []
				data['email'] = emailMatch.group(1)

			typeMatch = re.search(r'^Type:\s+(.+)$', l)
			if typeMatch:
				# if 'type' not in data:
				# 	data['type'] = []
				data['type'] = typeMatch.group(1)

			servicesMatch = re.search(r'^Services:\s+(.+)$', l)
			if servicesMatch:
				# if 'services' not in data:
				# 	data['services'] = []
				data['services'] = servicesMatch.group(1)


			# debug (f'{l}')

		output.append(data)



		# print("--- LEFTOVER ---")
		leftover = "\n".join(memory)
		page = re.search(r'2019 MHCA Directory\/Buyer’s Guide (\d+)', leftover)
		if page:
			for item in output:
				item['page'] = page.group(1)
		else:
			debug('Unable to determine page')

		for item in output:
			item['filename'] = filename

		# print(page.group(1) if page else "UNKNOWN Page")

	# print (output)
	if len(output) == 0:
		print (f'no match for file {filename}')
	return output

headers = [
	'filename',
	'page',

	'name',
	'tel',
	'address',

	'AddressNumber',
	'StreetName',
	'StreetNamePostType',
	# 'OccupancyType',
	# 'OccupancyIdentifier',
	'PlaceName',
	'StateName',
	'ZipCode',

	'contact',
	'email',
	'type',
	'services'
]

def buildRow(data):
	row = []
	for column in headers:
		item="!NONE!"
		if column in data:
			item = data[column]
		row.append(item)
	return row

import csv

with open('result.csv','w') as outputCSV:
	writer = csv.writer(outputCSV)

	writer.writerow(headers)

	for file in sorted(os.listdir(SRCDIR)):
		if not file.endswith('txt'):
			continue

		data = processOCR(SRCDIR+'/'+file)
		print(file, "\t", len(data))

		import json
		# print(json.dumps(data, indent=4))

		index = 0
		for item in data:

			if 'address' in item:
				addy = {}
				try:
					addy = usaddress.tag(item['address'])
					# print(addy)
					for k,v in addy[0].items():
						item[k] = v
				except Exception as e:
					print('invalid address')

			if 'page' not in item:
				item['page'] = 0
			item['page'] = float(item['page']) + index
			index += .1
			row = buildRow(item)
			# print(','.join(row))
			writer.writerow(row)




		

	







	

	
		

	# print (row)
	

	# import json
	# print(json.dumps(datadict, indent=4))










# 	ocrdict = processOCR(SRCDIR+'/'+file)
# 	# print (ocrdict)
# 	break

	

# import sys
# sys.exit(0)

