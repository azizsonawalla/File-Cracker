lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/', " ", "\f", "\n", "\t"]
all_characters = lowercase + uppercase + numbers + special

# ======================================================================================================================
# CLI Prompts
# ======================================================================================================================

# General
P_WELCOME = "\n\nWelcome to File Cracker\n\n"

# File location
P_ASK_FILEPATH = "Enter the path to the file you wish to crack:\n"
P_WRONG_FILEPATH = "\nHmmm...that doesn't look like a file. Try again.\n"
P_NOT_SUPPORTED_FILE = "\nSorry, {} files are not supported. Try again.\n"

# Password Guess Scope
P_SCOPE_INTRO = "Great! Now we'll need some information to help guess the password.\nThe more details you provide, " \
                "the faster we can crack the password.\n"
P_ASK_MIN_LEN = "Enter the MINIMUM length of the passwords we should try (integer value): \n"
P_ASK_MAX_LEN = "Enter the MAXIMUM length of the passwords we should try (integer value): \n"
P_BAD_VALUE = "Hmmm...that doesn't look like a usable value. Try again.\n"
P_CHAR_TYPES = "What type of characters does your password contain? Enter the corresponding numbers:\n\n" \
               "1. Lowercase alphabets\n" \
               "2. Uppercase alphabets\n" \
               "3. Numbers\n" \
               "4. Special Characters and symbols\n\n" \
               "For example, for lowercase and number characters enter 1,3\n"
