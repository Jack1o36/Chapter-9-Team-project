alphabet = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'y':23, 'x':24, 'z':25}
shift = 1

def main():
    pass
    
def get_shift(): #jamie
    pass
    
def choose_option(): #jamie
    pass
    
def get_message(): #jamie 
    pass
    
def create_key(shift):
    num = 0
    key = {}
    for item in alphabet:
        key[item] = num + shift
        num += 1
    return key
def encode(message, key): #jamie
    pass
    
def decode(message, key):
    alphabet = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'y':23, 'x':24, 'z':25}
    new_message = ''
    new_key = {}
    print(message)
    diff = 0
    for item in alphabet:
        if key[item] != alphabet[item]:
            diff = key[item] - alphabet[item]
        new_key[alphabet[item]] = item
    print(diff)
    print(new_key)
    for letter in message.lower():
        if letter.isalpha() == True:
            new_message += new_key[int((alphabet[letter])-diff)%26]
        else:
            new_message += letter
    print(new_message)