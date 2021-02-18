

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))



a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")



import json
data = {'username': 'jdoe', 'password': 's3cret'}
ugly = json.dumps(data)
pretty = json.dumps(data, indent=4, sort_keys=True)

print(data, type(data))
print(ugly, type(ugly))
print(pretty, type(pretty))


name = input('What is your name?\n')
print ('Hi, %s.' % name)
print(type(name))

