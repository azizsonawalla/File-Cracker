import win32com.client


class Excel:

    EXTENSIONS = ["xls", "xlsx"]
    OPENDOC = win32com.client.Dispatch("Excel.Application")

    def open(self, path, password="") -> bool:
        try:
            wb = self.OPENDOC.Workbooks.Open(path, False, True, None, password)
            print("Success! Password is: " + password)
            return True
        except:
            print("Incorrect password")
            return False