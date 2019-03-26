import sys
import win32com.client
import itertools
openedDoc = win32com.client.Dispatch("Excel.Application")
filename = "C:\\Users\\azizs\\Downloads\\ASTU.xlsx"

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/', " ", "\f", "\n", "\t"]
all_characters = lowercase + uppercase + numbers + special

password_max_length = 14

def try_open(password):
	try:
		wb = openedDoc.Workbooks.Open(filename, False, True, None, password)
		print("Success! Password is: "+password)
		return True
	except:
		print("Incorrect password")
		return False

def main():
	for i in range(4,password_max_length+1):
		for j in itertools.permutations(all_characters, i):
			j = list(j)
			password = "".join(j)
			print("trying: "+password)
			sys.stdout.flush()
			if try_open(password):
				return

if __name__ == '__main__':
	main()