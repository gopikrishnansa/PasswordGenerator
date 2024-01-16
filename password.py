import random

import random
import string


def numbers():
    global num
    num = []
    for i in range(1,5):
        random_integer = random.randint(1, 5)
        #print(random_integer)
        num.append(random_integer)
    #print(num)
    return num
def alphabets():
    global alph
    alph = []
    for j in range(1,5):
        random_alphabet_letter = random.choice(string.ascii_letters)
        alph.append(random_alphabet_letter)
    #print(alph)
    return alph

def combine():
    numbers()
    alphabets()
    pword = num+alph
    random.shuffle(pword)
    print("Generated password is ", *pword, sep='')
#def greet(character):

combine()