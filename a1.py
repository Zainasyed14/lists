import random
ListofNums= []
for i in range(50):
    num = random.randint(1,100)
    ListofNums.append(num)
print(ListofNums)
sum=0
for i in ListofNums:
    sum = sum + i
print("The sum of all the numbers from the list is : " , sum)