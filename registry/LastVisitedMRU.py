import re
from winreg import (
  ConnectRegistry,
  OpenKey,
  KEY_ALL_ACCESS,
  EnumValue,
  QueryInfoKey,
  HKEY_CURRENT_USER
)

class OpenSaveMRU():

    def __init__(self, ext):
        self.key = r"Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU"

    def enum_key(self, hive, subkey: str):
        with OpenKey(hive, subkey, 0, KEY_ALL_ACCESS) as key:
            num_of_values = QueryInfoKey(key)[1]
            for i in range(num_of_values):
                 values = EnumValue(key, i)
                 res = re.findall(r'\w+', str(values))
                 print(f"{str(res)}")


print('''
This key maintains a recently used program executable filename, and the folder path of a file to which the program has been used to open or save it.
''')

test = OpenSaveMRU("pdf")
with ConnectRegistry(None, HKEY_CURRENT_USER) as hkcu_hive:
     test.enum_key(hkcu_hive, f"{test.key}")
