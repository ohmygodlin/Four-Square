#!/usr/bin/python

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y', 'Z']

def get_key(key_input, alphabet):
	key = []
	for char in key_input:
		if char in alphabet and char not in key: # add the character to the matrix if it's valid and not already in the matrix
			key.append(char)
	for char in alphabet:
		if char not in key: # add the rest of the alphahet not appearing in the key to the matrix
			key.append(char)
	return key


def gen_matrix(key):
	matrix = []
	counter = 0
	for xcounter in xrange(5):
		x = []
		for ycounter in xrange(5):
			x.append(key[counter])
			counter += 1
		matrix.append(x)
	return matrix


def print_matrix(matrix):
	for counter in xrange(5):
		print "%c %c %c %c %c" % (matrix[counter][0], matrix[counter][1], matrix[counter][2], matrix[counter][3], matrix[counter][4])



def get_message():
	msg_input = raw_input()
	msg = []
	for char in msg_input.upper():
		if char.isalpha():
			msg.append(char)
	return ''.join(msg)


def decrypt(message, key1, key2):
	coords = []
	for char in alpha:
		if (char not in key1) and ( char not in key2) and (char not in message): 
			print("\nOmitting Letter: %s " % char)
			alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
			alphabet.remove(char)
			print("Alphabet Matrix:")
			matrix2 = gen_matrix(alphabet)
			print_matrix(matrix2)
			print("Keyed Matrix1:")
			alpha_key1 = get_key(key1, alphabet)
			matrix_key1 = gen_matrix(alpha_key1)
			print_matrix(matrix_key1)
			print("Keyed Matrix2:")
			alpha_key2 = get_key(key2, alphabet)
			matrix_key2 = gen_matrix(alpha_key2)
			print_matrix(matrix_key2)

			plaintext = []
			i = 0
			for d in message:
				if (i % 2 == 0) :
					coords1 = get_coords(d, matrix_key1)
					action = 0
				else:
					coords2 = get_coords(d, matrix_key2)
					action = 1
				i += 1
			
				if ( action ):
					x, y = ((coords1[0][0], coords2[0][1]))
					plaintext.append(matrix2[x][y])
					x, y = ((coords2[0][0], coords1[0][1]))
					plaintext.append(matrix2[x][y])
			print "Your decrypted message is  : %s \n" % ''.join(plaintext)


def get_coords(digraph, key_matrix):
	coords = []
	for char in digraph:
		for x in xrange(5):
			for y in xrange(5):
				if key_matrix[x][y] == char:
					coords.append((x,y))
	return coords
					

def main():
	print "Enter Key1:"
	key1 = raw_input().upper()

	print "Enter Key2:"
	key2 = raw_input().upper()

	print "Enter the message you would like to decrypt. \nThe only valid characters are the letters A-Z."
	message = get_message()
	print "The message you entered was: %s" % message
	plaintext = decrypt(message, key1, key2)

if __name__ == "__main__":
	main()
