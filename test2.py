from winreg import (
  ConnectRegistry,
  OpenKey,
  KEY_ALL_ACCESS,
  EnumValue,
  QueryInfoKey,
  HKEY_LOCAL_MACHINE,
  HKEY_CURRENT_USER
)
def enum_key(hive, subkey:str):
    with OpenKey(hive, subkey, 0, KEY_ALL_ACCESS) as key:
        num_of_values = QueryInfoKey(key)[1]
        for i in range(num_of_values):
            values = EnumValue(key, i)
            if values[0] == "LangID": continue
            print(*values[:-1], sep="\t")

with ConnectRegistry(None, HKEY_CURRENT_USER) as hkcu_hive:
    enum_key(hkcu_hive, r"Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU\pdf")
