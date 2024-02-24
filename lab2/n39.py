import random

A = []

for i in range(10):
    random_num = random.randint(-100, 100)
    A.append(random_num)
print(A)




print("минимальное число:", min(abs(i) for i in A))


for i in range(9, -1, -1):
    print(A[i])

B = []

for i in range(10):
    random_num = random.randint(1, 100)
    B.append(random_num)
print(B)

for i in range(10):
    A[i], B[i] = B[i], A[i]
print(A, B)


