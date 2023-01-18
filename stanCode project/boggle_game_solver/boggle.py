"""
File: boggle.py
Name: Jerry
----------------------------------------
TODO: To find all words for boggle game
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	This program play boggle game which is to find exit word in the dictionary within specific rule
	"""
	dic_lst = read_dictionary()

	l1 = input("1 row of letters: ")
	lst1 = l1.split()
	for i in range(len(lst1)):
		lst1[i] = lst1[i].lower()
		if len(lst1[i]) != 1:
			print("Illegal input")
			break

	l2 = input("2 row of letters: ")
	lst2 = l2.split()
	for i in range(len(lst2)):
		lst2[i] = lst2[i].lower()
		if len(lst2[i]) != 1:
			print("Illegal input")
			break

	l3 = input("3 row of letters: ")
	lst3 = l3.split()
	for i in range(len(lst3)):
		lst3[i] = lst3[i].lower()
		if len(lst3[i]) != 1:
			print("Illegal input")
			break

	l4 = input("4 row of letters: ")
	lst4 = l4.split()
	for i in range(len(lst4)):
		lst4[i] = lst4[i].lower()
		if len(lst4[i]) != 1:
			print("Illegal input")
			break

	total_alpha = []
	total_alpha.append(lst1)
	total_alpha.append(lst2)
	total_alpha.append(lst3)
	total_alpha.append(lst4)

	optimized_dic = {}  # dictionary for only length >= 4 words
	for word in dic_lst:
		if len(word) >= len(lst1):
			optimized_dic[word] = None

	start = time.time()
	word_search(total_alpha, optimized_dic)
	####################
	#                  #
	#       TODO:      #
	#                  #
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def word_search(total_alpha, dic):
	"""
	:param total_alpha: (list) total alphabet list
	:param dic: (dic) dictionary to check exist word
	:return: (str) all words that could be found in dictionary
	"""
	words = []  # use for collecting words
	l = len(total_alpha)
	for x in range(l):
		for y in range(l):
			current_s = ''
			ele = total_alpha[x][y]
			current_s += ele
			pos = (x, y)
			path = [pos]
			word_search_helper(total_alpha, dic, current_s, words, l, x, y, path)
	print(f'There are {len(words)} words in total.')


def word_search_helper(total_alpha, dic, current_s, words, l, x, y, path):
	if len(current_s) >= l:
		if current_s in dic and current_s not in words:
			print(f"Found \"{current_s}\"")
			words.append(current_s)

	# total_alpha[x][y] = ''  # set '' for the used alphabet
	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			neighbor_x = x+i
			neighbor_y = y+j
			if 0 <= neighbor_x < l and 0 <= neighbor_y < l:
				if (neighbor_x, neighbor_y) not in path:
					# Choose
					current_s += total_alpha[neighbor_x][neighbor_y]
					path.append((neighbor_x, neighbor_y))

					if has_prefix(current_s, dic):
						word_search_helper(total_alpha, dic, current_s, words, l, neighbor_x, neighbor_y, path)

					path.pop()
					current_s = current_s[:-1]


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		dic_lst = []
		for line in f:
			dic_lst.append(line.strip())
	return dic_lst


def has_prefix(sub_s, dic):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dic:
		if word[0] == sub_s[0]:
			if word.startswith(sub_s):
				return True
	return False


if __name__ == '__main__':
	main()
