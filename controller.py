import constants as c
import itertools
from time import time, sleep
from threading import Thread
import sys


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
        self.attempts_so_far = 0
        self.num_of_permutations = 0

    def run(self):
        # Get generator for password combinations
        all_passwords = self._generate_password_combinations()
        # Create a thread to report progress on console
        reporter = Thread(target=self._report_progress, args=(time(),), daemon=False)
        reporter.start()
        # Create worker threads to try all combinations
        for password in all_passwords:
            self.attempts_so_far += 1
            if self.type.open(path=self.path, password=password):
                print("Success! Password is {}".format(password))
                break
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
            self.num_of_permutations += pow(num_of_chars, r)
        print("There are {:.2e} possible passwords\n".format(self.num_of_permutations))

        for i in range(self.pass_min_len, self.pass_max_len + 1):
            for j in itertools.product(all_characters, repeat=i):
                j = list(j)
                password = "".join(j)
                yield password

    def _report_progress(self, start_time):
        while self.attempts_so_far == 0:
            continue
        while self.attempts_so_far != self.num_of_permutations:
            rate = (time()-start_time)/self.attempts_so_far
            eta = rate*(self.num_of_permutations-self.attempts_so_far)
            sys.stdout.write("\r{} passwords tried so far. Estimated time remaining is {}"
                             .format(self.attempts_so_far, self._sec_to_human_format(eta)))
            sys.stdout.flush()
            sleep(1)

    def _sec_to_human_format(self, seconds):
        if seconds < 60:
            return "{}s".format(seconds)
        mins, seconds = divmod(seconds, 60)
        if mins < 60:
            return "{}m {}s".format(mins, seconds)
        hours, mins = divmod(mins, 60)
        if hours < 24:
            return "{}h {}m".format(hours, mins)
        days, hours = divmod(hours, 24)
        if days < 365:
            return "{}days {}h".format(days, hours)
        years, days = divmod(days, 365)
        return "{}years {}days".format(years, days)
