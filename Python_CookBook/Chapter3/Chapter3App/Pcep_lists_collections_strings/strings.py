myString = "my string"
print(myString + " new string")


myString = 'my string'  + " second string"
myString = """ 
  This is a multi lines string 
 """

print(myString.encode())
myString = b"This is a byte string can only contain ascii code"
print(myString)

s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del s[0]
s.append(-1)
s.append(-23)
s.append(0)

s.sort()
print(s)



a = (1, 2, 3, 4, 5)
print(a)
woerterbuch = {"Germany" : "Deutschland", "Spain" : "Spanien", "Spain1" : "Spanien", "Spain2" : "Spanien"}
for key in woerterbuch:    
    print(woerterbuch[key])
print(len(woerterbuch))

is_contains = "Germany" not in woerterbuch
print(is_contains)

s_new = []
if s_new:
    print("The collection is not empty")
 
mytuple = ("apple", "banana", "cherry")
print(mytuple)


import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print("The type of loaded object is ", y)
print(y["age"])


print("Convert Python objects into JSON strings, and print the values:")
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
