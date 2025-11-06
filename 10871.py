# 1. N과 X를 입력받는다.
# 2. N번만큼 수를 입력받아서 A라는 수열에 저장시킨다
# 3. A를 돌면서 X보다 작은 값을 result에 저장한다.
# 4. Result를 출력한다

N = int(input())
X = int(input())
A = []
result = []


for i in range(N):
    temp = input()
    A.append(temp)
    
for i in A:
    if i < X:
        result.append(i)

for i in result:
    print(result)