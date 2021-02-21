

file = open("wasteland.txt", mode = "wt", encoding="utf-8")

file.write("what branches grow should be written in this position\n")
file.write("Willkomen in python\n")
file.write("what branches grow should be written in this position\n")
file.write("Out of this stony rubbish?\n")

position = file.seek(5)
file.write("__NEW_CONTENT_\n")

file.close() 


gfile = open("wasteland.txt", mode = "rt", encoding="utf-8")
content =  gfile.read(32)
print(content)

position = gfile.seek(5)
print(position)
all_lines = gfile.readline()  
print(f"current line is {all_lines}")
#
gfile.close()


import sys
f = open("wasteland.txt", mode='rt', encoding='utf-8')
for line in f:
    sys.stdout.write(line)
f.close()

def read_series(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [line.strip() for line in f]


result = read_series("wasteland.txt")
print(str(result))

def jungen():
    yield "vincent 1"
    yield "vincent 2"
    yield "vincent 3"
    yield "vincent 4"
    yield "vincent 5"            


for item in jungen():
    print(item)

#help(file)