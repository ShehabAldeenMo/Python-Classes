# -----------------------------------
# -- Modules => Create Your Module --
# -----------------------------------

import sys
sys.path.append(r"/home/shehabaldeen/Desktop/MyComputer") # add path that python need to search into
print(sys.path)

import shehab
print(dir(shehab))

shehab.sayHello("Ahmed")
shehab.sayHello("Shehab")
shehab.sayHello("Mohamed")

shehab.sayHowAreYou("Ahmed")
shehab.sayHowAreYou("Shehab")
shehab.sayHowAreYou("Mohamed")

# Alias

import shehab as ee

ee.sayHello("Ahmed")
ee.sayHello("Shehab")
ee.sayHello("Mohamed")

ee.sayHowAreYou("Ahmed")
ee.sayHowAreYou("Shehab")
ee.sayHowAreYou("Mohamed")

from shehab import sayHello

sayHello("Shehab")

from shehab import sayHello as ss

ss("Osama")