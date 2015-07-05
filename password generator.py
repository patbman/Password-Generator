import random
import string
from random import randint
import pickle
import uuid

a = eval(input("how long do you want the password to be: "))
filename=""
r = input("would you like to name the file or just generate a random name?(use either name or generate to answer): ")

if r == "name":
    filename=input("what would you like to name the file?: ") +".txt"
elif r == "generate":

    filename = str(uuid.uuid4())+ ".txt"

b=""

p=0

while True:
    
    c = random.choice(string.ascii_lowercase)

    d = randint(0,9)
    b= (b+c+str(d))
    p=p+2    

    
    if len(b) >= a:
        print(b)
        print(" ")
        print("Please note in the output file you will need to either delete or just ignore €X€")

        file = open(filename, "wb")
        pickle.dump(str(b), file)
        file.close()
        break
        
# By Patrick Bowden
