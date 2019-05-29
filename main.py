import os
from controller import Controller

config = {
	"path": None,
	"pass_min_length": None,
	"pass_max_length": None,
	"max_threads": None,
	"lowercase": True,
	"uppercase": True,
	"numbers": True,
	"special": True,
	"possible": []
}

def capture_input():
	print("\n\nWelcome to Excel Password Cracker\n\n")
	while True:
		print("Enter the path to the file you wish to crack:\n")
		file_path = os.path.abspath(str(input()).replace("\"", ""))
		if not os.path.isfile(file_path):
			print("\nHmmm...that doesn't look like a file. Try again:\n")
			continue
		filename, file_extension = os.path.splitext(file_path)
		if file_extension not in SUPPORTED_EXTENSIONS:
			print("\nSorry, {} files are not supported. Try again:\n".format(file_extension))
			continue


def main():
	config = capture_input()
	c = Controller(config)
	c.run()
	return


if __name__ == '__main__':
	main()