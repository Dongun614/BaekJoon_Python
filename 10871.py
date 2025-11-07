import sys

try:
    N, X = map(int, sys.stdin.readline().split())
except ValueError:
    sys.exit()
    
try:
    A = list(map(int, sys.stdin.readline().split()))
except ValueError:
    sys.exit()
    
result = []

for a in A:
    if a < X:
        result.append(str(a))
        
print(" ".join(result))