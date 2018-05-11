import twl
import numpy as np

array = np.array([['!s','!e','!x',0,0,0,0,0,0,0,'!x'],
				  [0,0,0,0,0,0,0,0,0,0,0],
				  [0,0,0,0,0,0,0,0,0,0,0],
				  [0,0,0,0,0,'!a',0,0,0,0,0],
				  [0,0,0,0,0,0,0,0,0,0,0],
				  [0,0,0,0,0,0,0,0,0,0,0],
				  [0,0,0,0,0,0,0,0,0,0,0],
				  [0,0,0,0,0,0,0,0,0,0,0],
				  [0,0,0,0,0,0,0,0,0,0,0],
				  [0,0,0,0,0,0,0,0,0,0,0],
				  [0,0,0,0,0,0,0,0,0,0,'!t']])

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

#print(array[0][1]) # a
#print(score["w"]) # 4

def findStart():

	start_x = None
	start_y = None
	wordLength = 0

	for y in range(11):
		for x in range(11):
			if array[y][x][0] is '!':
				wordLength += 1
				if start_x is None:
					start_x = x
					start_y = y

	return wordLength, start_x, start_y


def possCheck(lenword, x, y):
	word_h = []
	word_v = []

	for i in range(lenword):
		if array[y][x+i][0] is '!':
			word_h.append(array[y][x+i][1])



	for i in range(lenword):
		if array[y+i][x][0] is '!':
			word_v.append(array[y+i][x][1])


	if len(word) > 1:
		return word
	else:
		del word[:]

	if len(word) > 1:
		return word
	else:
		print("Fant ingen nye ord! Ordet må bestå av flere enn 1 bokstav.")
		exit()



def traverse():
	pass

length_of_word, start_x , start_y = findStart()

word_excl = possCheck(length_of_word, start_x, start_y)

print(word_excl)

word = ''.join(word_excl)

print(word)

print(twl.check(word))


#print(length_of_word, start_x, start_y)
