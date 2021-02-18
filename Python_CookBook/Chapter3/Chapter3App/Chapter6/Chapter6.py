import json
 


currentMax = max([3,6,2,1,9])
print("The maxium is {}".format(currentMax) )
ref = None
print(ref)


# read file

def read_json_file():
    with open('example.json', 'r') as myfile:
        data=myfile.read()
        # parse file
        readObject = json.loads(data)
        # show values
        print(id(readObject))
        print("usd: " + str(type(readObject)))
        print("usd: " + str(readObject['usd']))
        print("eur: " + str(readObject['eur']))
        print("gbp: " + str(readObject['gbp']))
 


def read_text_file_with_as():
    with open("woerterbuch.txt", "r") as file:
         allLines = file.readlines()
         for line in allLines:
             print(id(line))
             print(line)


def read_text_file():
    fobj = open("woerterbuch.txt", "r")
    for line in fobj:
        line = line.strip()
        zuordnung = line.split(" ")       
        woerter[zuordnung[0]] = zuordnung[1]
        print(woerter[zuordnung[0]])
    fobj.close()

#while True:
#    wort = input("Geben Sie ein Wort ein: ")
#    if wort in woerter:
#        print("Das deutsche Wort lautet:", woerter[wort])
#    else:
#        print("Das Wort ist unbekannt")


def main():
    read_json_file()
    read_text_file_with_as()



if __name__ == '__main__':
   main()
