a = int(input("Enter the number\n"))
b = 1
if a % 2 == 0:
    a = a - 1
for i in range(a):
    print(b, end=" ")
    b += 2
