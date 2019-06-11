import itertools
from time import time, sleep
from threading import Thread
import sys
import multiprocessing
from queue import Queue
from shutil import copyfile
import os
import constants as c


class Controller:

    FILE_COPY_NAME_FORMAT = "{}_{}"

    def __init__(self):
        self.path = None
        self.type = None
        self.pass_min_len = None
        self.pass_max_len = None
        self.lowercase = False
        self.uppercase = False
        self.numbers = False
        self.special = False

        self.attempts_so_far = 0
        self.num_of_permutations = 0

        self.password_queue = None
        self.correct_password = None

    def run(self):
        # Get generator for password combinations
        all_passwords = self._generate_password_combinations()
        # Create a thread to report progress on console
        reporter = Thread(target=self._report_progress, args=(time(),), daemon=False)
        reporter.start()
        # Create worker threads to try all combinations
        self.password_queue = Queue()
        thread_count = 2*multiprocessing.cpu_count()
        for i in range(0, thread_count):
            # make a copy
            filename, file_extension = os.path.splitext(self.path)
            new_path = self.FILE_COPY_NAME_FORMAT.format(filename, i).join(self.path.rsplit(filename, 1))
            copyfile(str(self.path), new_path)
            thread = Thread(target=self._run_attack, name="thread_{}".format(i), args=(new_path,), daemon=False)
            thread.start()
        for password in all_passwords:
            if self.correct_password:
                self._cleanup(thread_count)
                break
            self.password_queue.put(password)

    def _run_attack(self, file_path):
        while not self.correct_password:
            if not self.password_queue.empty():
                password = self.password_queue.get()
                if self.type.open(path=file_path, password=password) and not self.correct_password:
                    self.correct_password = password
                    print(c.PASSWORD_SUCCESS.format(password))
                    break
                self.attempts_so_far += 1

    def _cleanup(self, thread_count, filename):
        # delete all files
        for i in range(0, thread_count):
            file_to_delete = self.FILE_COPY_NAME_FORMAT.format(filename, i).join(self.path.rsplit(filename, 1))
            os.remove(file_to_delete)

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
        for r in range(0, num_of_chars+1):
            self.num_of_permutations += pow(num_of_chars, r)
        print(c.TOTAL_PERM.format(self.num_of_permutations))

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
            sys.stdout.write(c.PROGRESS_REPORT.format(self.attempts_so_far, self._sec_to_human_format(eta)))
            sys.stdout.flush()
            sleep(1)

    def _sec_to_human_format(self, seconds):
        if seconds < 60:
            return "{}s".format(int(seconds))
        mins, seconds = divmod(seconds, 60)
        if mins < 60:
            return "{}m {}s".format(int(mins), int(seconds))
        hours, mins = divmod(mins, 60)
        if hours < 24:
            return "{}h {}m".format(int(hours), int(mins))
        days, hours = divmod(hours, 24)
        if days < 365:
            return "{}days {}h".format(int(days), int(hours))
        years, days = divmod(days, 365)
        return "{}years {}days".format(years, int(days))
