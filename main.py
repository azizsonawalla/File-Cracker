import os
from controller import Controller
from FileTypes.Excel import Excel
import constants as c


# File types supported
FILE_TYPES = [
	Excel()
]


def _capture_input() -> Controller:
	controller: Controller = Controller()
	supported_file_extensions: list = _generate_supported_file_extensions()
	print(c.P_WELCOME)

	# Get file location and validate
	while True:
		file_path = os.path.abspath(str(input(c.P_ASK_FILEPATH)).replace("\"", ""))
		if not os.path.isfile(file_path):
			print(c.P_WRONG_FILEPATH)
			continue
		filename, file_extension = os.path.splitext(file_path)
		if file_extension not in supported_file_extensions:
			print(c.P_NOT_SUPPORTED_FILE.format(file_extension))
			print(supported_file_extensions)
			continue
		controller.path = file_path
		controller.type = _find_file_type_class(file_extension)
		break

	# Get password guess scope
	print(c.P_SCOPE_INTRO)
	while True:
		pass_min_len = input(c.P_ASK_MIN_LEN)
		try:
			pass_min_len = int(pass_min_len)
			if pass_min_len < 0:
				raise ValueError
			controller.pass_min_len = pass_min_len
			break
		except ValueError:
			print(c.P_BAD_VALUE)
			continue
	while True:
		pass_max_len = input(c.P_ASK_MAX_LEN)
		try:
			pass_max_len = int(pass_max_len)
			if pass_max_len < 0:
				raise ValueError
			controller.pass_max_len = pass_max_len
			break
		except ValueError:
			print(c.P_BAD_VALUE)
			continue
	while True:
		char_types = str(input(c.P_CHAR_TYPES))
		choice_confirmation = ""
		if "1" in char_types:
			controller.lowercase = True
			choice_confirmation += "Lowercase\n"
		if "2" in char_types:
			controller.uppercase = True
			choice_confirmation += "Uppercase\n"
		if "3" in char_types:
			controller.numbers = True
			choice_confirmation += "Numbers\n"
		if "4" in char_types:
			controller.special = True
			choice_confirmation += "Special Characters\n"
		if choice_confirmation == "":
			print("No character types selected. Please make a choice.\n")
			continue
		else:
			print("\nYou have chosen the following character types: \n" + choice_confirmation)
			break

	return controller


def _find_file_type_class(extension: str):
	for file_type in FILE_TYPES:
		if extension in file_type.EXTENSIONS:
			return file_type
	raise Exception("Couldn't find a file type for extension {}".format(extension))


def _generate_supported_file_extensions() -> list:
	supported_file_extensions = []
	for file_type in FILE_TYPES:
		supported_file_extensions.extend(file_type.EXTENSIONS)
	return supported_file_extensions


def main():
	controller: Controller = _capture_input()
	controller.run()
	return


if __name__ == '__main__':
	main()