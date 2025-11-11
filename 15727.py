import sys
import math

try:
    distance = int(sys.stdin.readline())
    
except ValueError:
    sys.exit()
    
print(math.ceil(distance / 5))
