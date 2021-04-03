import re
from winreg import (
  ConnectRegistry,
  OpenKey,
  KEY_ALL_ACCESS,
  EnumValue,
  QueryInfoKey,
  HKEY_LOCAL_MACHINE,
  HKEY_CURRENT_USER
)

# https://www.python.org/dev/peps/pep-0514/
# https://python.plainenglish.io/digital-forensics-accessing-the-windows-registry-with-python-f32e138691b0

class OpenSaveMRU():
    def __init__(self, ext):
        self.key = r"Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU"
        self.ext = str(ext)

    # def enum_keys(self, key):
    #     i = 0
    #     while True:
    #         try:
    #             yield winreg.EnumKey(key, i)
    #         except OSError:
    #             break
    #         i += 1

    # def recently_opened(self):
    #     recently_opened_or_saved_files = []
    #     with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.key) as company_key:
    #         for self.tag in self.enum_keys(company_key):
    #             if self.tag == 'xlsx' or 'xlsm' or 'txt' or 'pptx' or 'pptm' or 'pdf' or 'dotm' or 'DAT':
    #                 recently_opened_or_saved_files.append(self.tag)
    #     return recently_opened_or_saved_files

    def enum_key(self, hive, subkey: str):
        with OpenKey(hive, subkey, 0, KEY_ALL_ACCESS) as key:
            num_of_values = QueryInfoKey(key)[1]
            print(f"[*]{self.ext}[*]")
            for i in range(num_of_values):
                values = EnumValue(key, i)
                res = re.findall(r'\w+', str(values))
                #print(f"{str(res)}")

    # def loop_to_extract(self):
    #     with ConnectRegistry(None, HKEY_CURRENT_USER) as hkcu_hive:
    #         self.enum_key(hkcu_hive, f"{self.key}\{self.ext}")


print('''
This key maintains a list of recently opened or saved files,
including those who opened or saved within a web browser but not including documents that are opened or saved via Microsoft Office programs.
''')
test = OpenSaveMRU("pdf")
with ConnectRegistry(None, HKEY_CURRENT_USER) as hkcu_hive:
     test.enum_key(hkcu_hive, f"{test.key}\{test.ext}")
