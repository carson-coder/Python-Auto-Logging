import sys
from datetime import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class StdOut(object):
    def __init__(self,txtctrl):
        self.txtctrl = txtctrl
    def write(self,string):
        if string == "\n":
            self.txtctrl.write("\n")
        elif "\n" not in string:
            self.txtctrl.write(f"{bcolors.OKGREEN}{bcolors.BOLD}Print At {datetime.now().strftime('%I:%M %p')}: "+string+bcolors.ENDC)
        elif "\n" in string:
            for i in range(len(string.split("\n"))):
                self.txtctrl.write(f"{bcolors.OKGREEN}{bcolors.BOLD}Print At {datetime.now().strftime('%I:%M %p')} {bcolors.OKCYAN}Line "+str(i+1)+bcolors.OKGREEN+": "+string.split("\n")[i]+bcolors.ENDC)
                if i != len(string.split("\n")) - 1:
                    self.txtctrl.write("\n")
    def flush(self):
        self.txtctrl.flush()

class StdErr(object):
    def __init__(self,txtctrl):
        self.txtctrl = txtctrl
        self.nline = True
    def write(self,string):
        if string == "\n":
            self.txtctrl.write("\n")
        elif self.nline:
            self.txtctrl.write(f"{bcolors.FAIL}{bcolors.BOLD}Error At {datetime.now().strftime('%I:%M %p')}: "+string.split("/n")[len(string.split("/n"))-1]+bcolors.ENDC)
        else:
            self.txtctrl.write(bcolors.FAIL+bcolors.BOLD+string.split("/n")[len(string.split("/n"))-1]+bcolors.ENDC)
        if "\n" not in string:
            self.nline = False
        elif "\n" in string:
            self.nline = True
    def flush(self):
        self.txtctrl.flush()

sys.stdout = StdOut(sys.stdout)
sys.stderr = StdErr(sys.stderr)

print("This is test of my output system")
print("Hello\nThis Is Text\nThis Is More Text")
raise Exception("Error")