'''
Use by calling Unscrabble.py WORD
To sort by length, Unscrabble.py WORD char
'''
import argparse
import time
import getdef

def tally_score(word):
	score = 0
	scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
     "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
     "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
     "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
     "x": 8, "z": 10}

	for letter in word:
		score += scores[letter]
	return score

def by_length(found_words):
	for word in sorted(found_words, key=len, reverse=True):
		print word + "\t" + str(found_words[word])

def by_value(found_words):
	for word in sorted(found_words, key=found_words.get, reverse=True):
		print word + "\t" + str(found_words[word])

	
def is_rack_in_word(rack ,word):
		used_letters = ''
		for letter in rack.lower():
			if letter in word:
				rack = rack.replace(letter, '', 1)				
				used_letters = used_letters + letter
				if sorted(used_letters) == sorted(word) and len(used_letters) > 1:
					return True
				
def create_word_score_dictionary(words):
	scored_words = {}
	for word in words:
		scored_words[word] = tally_score(word)
	return scored_words	

def main(rack, sort):
	start = time.clock()
	# filename = 'sowpods.txt'
	filename = 'scrabble.txt'

	wordlist = []
	with open(filename, 'r') as f:
		for line in f:
			if len(line) < 8: #Filtering out letters longer than possible in scrabble
				wordlist.append(line.strip())

	valid_words = []
	for word in wordlist:
		if is_rack_in_word(rack, word):
			valid_words.append(word)

	found_words = create_word_score_dictionary(valid_words)
	
	if sort.lower() != "v":	
		by_length(found_words)
	else:
		by_value(found_words)
	
	print len(valid_words), " possible words using ", rack.upper()
	end = time.clock()
	print "Elapsed time ", end-start, " seconds."
	while True:
		word = raw_input("Type word you would like to define. ('q' to quit)\t")
		if word.lower() == 'q':
			break
		print getdef.define(word)
		print "-" * 72

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('rack',type=str)
	parser.add_argument('sort', nargs='?',type=str, default='v')
	args = parser.parse_args()
	if len(args.rack) > 7:
		print "7 letters only"
		exit()	
	main(args.rack, args.sort)