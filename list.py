s1 = ["apples", "mango", "monky", "donky", "dog", "dog"]
if "apple" in s1:
    print("Yes, 'apple' is in the fruit s1")
else:
    print("welcom to new query")




s1 = ["apple","mango","monky","donky","dog","dog"]
s2 = [45,20,25,30,44]
s3 = [45,"ali",30,"apple"]

print(type(s3))

s =list(("apple","mango","orange",))

print(s)

s1 = ["apple","mango","monky","donky","dog","dog"]
print(s1[1])
print(s1[5])
print(s1[2:5])
print(s1[:4])

s1 = ["apple","mango","monky","donky","dog","dog"]
s1[5] = "mango"
print(s1)

s1 = ["apple","mango","monky","donky","dog","dog"]
s1[1:2] = "banana","orange"
print(s1)

s1 = ["apple", "banana", "mango"]
s1.insert(2,'watermelon')
print(s1)

s1 = ["apple", "mango", "banana"]
s2 = ["orange", "graps"]
s1.extend(s2)
print(s1)

s1 = ["banana", "mango", "sweet"]
s1.remove("banana")
print(s1)

s1 = ["banana", "mango"]
s2 = ["banana1"]
s1.extend(s2)
print(s1)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(0)
print(thislist)

#delete this list

s1 = ["banana", "apple", "mango"]
del s1

s1 = ["banana", "apple", "mango"]
s1.clear()
print(s1)