
list=[]
sum=0
counter=0

for i in range(10):
    number=int(input('Enter a number: '))
    list.append(number)
    sum+=number
    counter+=1

print(list)
print(min(list))
print(max(list))
print(sum)
print(sum/counter)
