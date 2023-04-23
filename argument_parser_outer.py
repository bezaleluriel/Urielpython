import  subprocess
# run the "argument_parser.py" from outer file
# x = subprocess.run(["python", "argument_parser.py", "5"])
x = subprocess.Popen(["python", "argument_parser.py", "5"])
print(x.returncode)
x.communicate()
print(x.returncode)
