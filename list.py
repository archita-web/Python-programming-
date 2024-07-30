marks = [87,64,33,95,76]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
marks[0] = 'arjun'
print(marks)
str = 'hello'
print(str[0])
marks[1:4]

#list are mutable. string are immutable
list = [12,1,3]

print(list.append(4))
print(list.sort(reverse=True))
print(list)
print(list.insert(1,5))
print(list.remove(1))
print(list.pop(2))