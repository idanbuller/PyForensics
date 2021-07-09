import subprocess

data = subprocess.check_output(['wmic', 'qfe', 'list']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "microsoft" in i]
for i in profiles:
    try:
        print(f"{i}")
    except IndexError:
        print("{:<30}|  {:<}".format(i, ""))
