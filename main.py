import os
from controller import Controller
"""
config = {
	"path": None,
	"type": None,
	"pass_min_length": None,
	"pass_max_length": None,
	"max_threads": None,
	"lowercase": True,
	"uppercase": True,
	"numbers": True,
	"special": True,
	"possible": []
}
"""


def capture_input() -> dict:
	config = {}
	supported_file_types = []  # TODO
	print("\n\nWelcome to File Cracker\n\n")
	while True:
		file_path = os.path.abspath(str(input("Enter the path to the file you wish to crack:\n")).replace("\"", ""))
		if not os.path.isfile(file_path):
			print("\nHmmm...that doesn't look like a file. Try again:\n")
			continue
		filename, file_extension = os.path.splitext(file_path)
		if file_extension not in supported_file_types:
			print("\nSorry, {} files are not supported. Try again:\n".format(file_extension))
			continue
		config["path"] = file_path
		break
	return config


def main():
	config = capture_input()
	c = Controller(config)
	c.run()
	return


if __name__ == '__main__':
	main()