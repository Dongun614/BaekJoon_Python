import sys
try:
    jaehwan = sys.stdin.readline()
    doctor = sys.stdin.readline()
except ValueError:
    sys.exit()
    

if len(jaehwan) < len(doctor):
    print("no")
else:
    print("go")