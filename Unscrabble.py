import argparse


def main(tiles):
	wordlist = []
	#using with automaticall closes the file when you moveo ut of the code, this is equivalent to f.open, f.close, this is a STANDARD when working with files in PYTHON
	with open('sowpods.txt', 'r') as f:
		for line in f:
			wordlist.append(line.strip())

	valid_words = []
	for word in wordlist:
		rack = tiles
		# rack = 'ZAEFIEE'
		used_letters = ''
		# print word + "\t",
		for letter in rack.lower():
			if letter in word:
				
				rack = rack.replace(letter, '', 1)
			
				used_letters = used_letters + letter
				# index = rack.find(letter)
				# print "Letter ", letter, " was taking out of the rack"
				# print "Current Rack:\t" ,rack
				# temp = rack[index-1]
				# print "takes out ", letter, " from the rack"
				# temp2 = rack[index+1:]
				# temp = temp + temp2
				# rack = temp
			# 	# print rack
			# print "used letters\t", used_letters
			# print " word\t", word
				if sorted(used_letters) == sorted(word) and len(used_letters) > 1:
					valid_words.append(word)

	# This orders valid_words using the length of each word, reverse makes it Greatest to Smallest, if you leave it out it is by default a-z, smallest to largest
	for word in sorted(valid_words, key=len, reverse = True):
		print word




parser = argparse.ArgumentParser()
parser.add_argument('rack',type=str)
args = parser.parse_args()
main(args.rack)