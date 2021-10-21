a = [int(i) for i in input("Enter the elements").split()]
b = {}
count = 0
for i in range(1, 10):
    for j in a:
        if j % i == 0:
            count+=1
    b[i] = count
    count = 0
print(b)
