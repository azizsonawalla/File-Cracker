import constants as c
import itertools


class Controller:

    def __init__(self):
        self.path = None
        self.type = None
        self.pass_min_len = None
        self.pass_max_len = None
        self.lowercase = False
        self.uppercase = False
        self.numbers = False
        self.special = False
        self.threads = 8

    def run(self):
        # Get generator for password combinations
        all_passwords = self._generate_password_combinations()
        # Create a thread to report progress on console
        # Create worker threads to try all combinations
        return

    def _generate_password_combinations(self):
        all_characters = []
        if self.lowercase:
            all_characters.extend(c.lowercase)
        if self.uppercase:
            all_characters.extend(c.uppercase)
        if self.special:
            all_characters.extend(c.special)
        if self.numbers:
            all_characters.extend(c.numbers)

        num_of_chars = len(all_characters)
        num_of_permutations = 0
        for r in range(0, num_of_chars+1):
            num_of_permutations += pow(num_of_chars, r)
        print("There are {:.2e} possible passwords\n".format(num_of_permutations))

        for i in range(self.pass_min_len, self.pass_max_len + 1):
            for j in itertools.permutations(all_characters, i):
                j = list(j)
                password = "".join(j)
                yield password
