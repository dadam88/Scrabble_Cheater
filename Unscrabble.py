import argparse

def main(tiles):

	scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

	wordlist = []
	
	with open('sowpods.txt', 'r') as f:
		for line in f:
			wordlist.append(line.strip())

	valid_words = []
	for word in wordlist:
		rack = tiles
		used_letters = ''
		for letter in rack.lower():
			if letter in word:
				rack = rack.replace(letter, '', 1)
				used_letters = used_letters + letter
				if sorted(used_letters) == sorted(word) and len(used_letters) > 1:
					valid_words.append(word)
	
	for word in sorted(valid_words, key=len, reverse = True):
		score = 0
		for letter in word:
			score += scores[letter]

		print word + "\t" +  str(score)

parser = argparse.ArgumentParser()
parser.add_argument('rack',type=str)
args = parser.parse_args()
main(args.rack)