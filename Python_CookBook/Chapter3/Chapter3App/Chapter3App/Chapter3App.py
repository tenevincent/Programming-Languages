

print(' Hello Welt')

myList = []
myList.append(1)
myList.append(2)
myList.append(3)
print(myList)

dict_values = {"name" : "Vincent De Paul", "schlüssel2" : "wert2"}
print(dict_values["name"])

name = 23
name = "Vincent De Paul"
print(name)
if name:
   print("The value is positiv!")

liste = [2,7,3,2,7,8,4,2,5]
liste.sort()
print(liste)

# Ein Beispiel mit Kommentaren
print("Hallo Welt!") # Simple Hallo-Welt-Ausgabe

i = 10
if i == 10:
    print("Falsch eingerückt")

x = 12
if x < 1 or x > 5:
    print("x ist kleiner als 1 ...")
    print("... oder größer als 5")

if x == 1:
    print("x hat den Wert 1")
elif x == 2:
    print("x hat den Wert 2")

if x == 1:
    print("x hat den Wert 1")
elif x == 2:
    print("x hat den Wert 2")
elif x == 3:
    print("x hat den Wert 3")
else:
    print("x hat den Wert {}".format(x))



for x in [1,2,3]:
    print(x)

for i in range(1, 10, 2):
    print(i)

def bytes2int(b):
    res = 0
    for x in b[::-1]:
        res = (res << 8) + x
    return res

'''
f = open("bild.bmp", "rb")
f.seek(18)
print("Breite:", bytes2int(f.read(4)), "px")
print("Höhe:", bytes2int(f.read(4)), "px")
f.seek(2, 1)
print("Farbtiefe:", bytes2int(f.read(2)), "bpp")
f.close()
'''

def read_json_file():
    import json
    with open('input.json', 'r') as input:
        obj = json.load(input)
        print('Hello, ', obj['name'])

def write_json_file():
    import json
    with open('input.json', 'r') as input:
        obj = json.load(input)
        with open('output.txt', 'w') as output:
            output.write(obj['name'] + "'s Hobbies:\n")
            for hobby in obj['hobbies']:
                output.write(hobby + "\n")



read_json_file()

write_json_file()
