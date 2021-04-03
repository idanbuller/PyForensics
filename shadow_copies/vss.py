import subprocess

class Shadow_Copies():
  def __init__(self):
    pass

  def list_shadows(self):
    p = subprocess.Popen('vssadmin list shadows', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
      print(line)
    retval = p.wait()