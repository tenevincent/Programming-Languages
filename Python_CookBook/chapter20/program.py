

import sys
sys.path.append("main.libs")
import main.libs as library
import main.libs.sub

import main.libs.fakultaet as fac
from urllib import  request
import main.libs.sub.kehr as sub




print(fac.fak(4))

import importlib
math = importlib.import_module("math")
print(math.cos(0))


print(library)
print(sub)
print(sub.kehr(2))