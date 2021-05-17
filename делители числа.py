numbers = int(input())
deliteli =[]
for i in range(numbers,0,-1):
    if numbers % i ==0 :
        deliteli.append(i)
print(deliteli)
