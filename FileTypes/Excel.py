import win32com.client


class Excel:

    EXTENSIONS = [".xls", ".xlsx"]
    OPENDOC = win32com.client.Dispatch("Excel.Application")

    def open(self, path, password="") -> bool:
        try:
            self.OPENDOC.Workbooks.Open(path, False, True, None, password)
            return True
        except:
            return False