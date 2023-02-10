#my first python list
names=["keith","james","kinyua","tiffan"]
# numbers=[3,6,8,4]
decimals=[45.9,89.9,10.1]
print(names[0])
# my second python list
numbers=[45,67,34,76,23,45,78]

#print(len(numbers))# get the legth on my list

# print(sum(numbers))

# for i in range(len(numbers)):
#     print(numbers[i])
#listmethods
#index
# print(numbers.index(23))
print(names.index("james"))

#append

#before appending
for i in range(len(numbers)):
    print (numbers[i])
print("/n")
numbers.append(90)

print(numbers)

#after appending
for i in range(len(numbers)):
    print(numbers[i])
#count
print(numbers.count(7))
#pop
print(numbers.pop(2))
#insert
numbers.insert(2,100)
for i in range(len(numbers)):
    print(numbers[i])
#sort-arranges the list in ascending order
for i in range(len(numbers)):
    print(numbers[i])
#multiplying a list 
fives=[5]*5
fives
#slicing list 
nums=[12,13,34,65,23,54]



max(nums)

min(nums)
#creating list

for i in range(10):
    #insert elements into the list
    nums.append(i)

for i in range(len(nums)):
    print(nums[i])
