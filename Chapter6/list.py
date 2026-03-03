user = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []

print("Dave" in emptylist)

print(user[0])
print(user[-2])

print(user.index('Sara'))

print(user[0:2])
print(user[1:])
print(user[-3:-1])

print(len(data))

user.append('Elsa')
print(user)

user += ['Jason']
print(user)

user.extend(['Robert', 'Jimmy'])
print(user)

# user.extend(data)
# print(user)

user.insert(0, 'Bob')
print(user)

user[2:2] = ['Eddie', 'Alex']
print(user)

user[1:3] = ['Robert', 'JPJ']
print(user)

user.remove('Bob')
print(user)

print(user.pop())
print(user)

del user[0]
print(user)

#del data
data.clear()
print(data)

user[1:2] = ['dave']
user.sort()
print(user)

user.sort(key=str.lower)
print(user)

nums = [4,42,78,1,5]
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1,"Neil",True])
print(mylist)

#Tuples

mytuple = tuple(('Dave',42,True))

anothertuple = (1,4,2,8,2,2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))
