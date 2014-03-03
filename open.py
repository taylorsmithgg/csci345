import glob
import chardet
import os.path
import collections

dictionary = []
postings = {}

dictfile = open('dictionary.txt','w')

def findkey():
	(val,key) = line.split()
	postings[str(val),infile] = key
	dictionary.append(str(val))

def findbrokenkey():
	key = str(next(f, None)).rstrip('\n')
	if key == 'None':
		pass
	else:	
		val = line
		postings[str(val),infile] = key
		dictionary.append(str(val))

def writefiles():
	for infile in glob.glob('input/*'):
		for entry in dictionary:
			try:
				print(entry)
				output = open('postings/' + entry + '.txt','a')
				output.write(infile + " " + postings[entry,infile] + "\n")
				output.close
			except:
				pass
	print("Finished writing postings")
def writedict():
	for query in dictionary:
		dictfile.write(query + "\n")

def getpostings(input):
	for files in glob.glob('postings/*'):
		if input in files:
			result = open(files).read()
			print(result)

for infile in glob.glob('input/*'):
	rawdata = open(infile, "rb").read()
	result = chardet.detect(rawdata)
	charenc = result['encoding']
	with open(infile, encoding = charenc) as f:
		for line in f:
			line = line.strip()
			try:
				findkey()
			except:
				findbrokenkey()
print("Finished scanning files")
dictionary = sorted(set(dictionary))
writedict()
writefiles()