alphabet = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'y':23, 'x':24, 'z':25}
shift = 1

def main():
    shift = get_shift()
    message = get_message()
    key = create_key(shift)
    value = choose_option()
    if value == True:
        encode(message, key)
    else:
        decode(message, key)
def get_shift(): #jamie
    #get_shift will prompt the user for the shift value and return the value as a string
    #it will use variable 'shift_value' as the value
    
    #take input
    shift_value = input("Enter a number 1 - 25 for your encoding shift value: ")
    
    #checking to be a number
    while shift_value.isdigit() == False:
        shift_value = input("Enter a number 1 - 25 for your encoding shift value (no letters or characters): ")
        
    #checking to be a letter
    while 1 > int(shift_value) or 25 < int(shift_value):
        shift_value = input("Enter a number 1 - 25 for your encoding shift value: ")
    
    shift_value = str(shift_value)
    
    return shift_value
     
def choose_option(): #jamie
    #choose_option will prompt the user to choose to encode or decode
    #it will return true if the user chooses encode and false if the user chooses decode
    #validate to only accept the appropriate prompts for encode or decode
    
    #take initial input
    option = input('Choose \'1\' to encode or \'2\' to decode: ')
     
    #check that option is a number
    while option.isdigit() == False:
        option = input("Please only select \'1\' to encode or \'2\' to decode: ")
    
    #check that option is only 1 or 2
    while int(option) < 1 or int(option) > 2:              
        option = input('Please only select \'1\' to encode or \'2\' to decode: ')
    
    #return true
    if int(option) == 1:
        return True
    
    #return false
    else:
        return False
    
def get_message(): #jamie
    #get_message should prompt the user to enter a message that will be encoded or decoded
    #it should return that message
    #it will be variable 'message'
    
    #get user input
    message = input("Enter a message to encode or decode: ")
    
    return message
    
def create_key(shift):
    num = 0
    key = {}
    for item in alphabet:
        key[item] = num + shift
        num += 1
    return key



def encode(message, key): #jamie
    #encode will accept message as a string and key as a dictionary
    #it will encode the message using the key and return the encoded message as string
    #the encoded message will be variable 'encoded_message'
    alphabet = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'y':23, 'x':24, 'z':25}
    new_message = ''
    new_key = {}
    diff = 0
    for item in alphabet:
        if key[item] != alphabet[item]:
            diff = key[item] - alphabet[item]
        new_key[alphabet[item]] = item
    for letter in message.lower():
        if letter.isalpha() == True:
            new_message += new_key[int((alphabet[letter])+diff)%26]
        else:
            new_message += letter
    print(new_message)
    
def decode(message, key):
    alphabet = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'y':23, 'x':24, 'z':25}
    new_message = ''
    new_key = {}
    diff = 0
    for item in alphabet:
        if key[item] != alphabet[item]:
            diff = key[item] - alphabet[item]
        new_key[alphabet[item]] = item

    for letter in message.lower():
        if letter.isalpha() == True:
            new_message += new_key[int((alphabet[letter])-diff)%26]
        else:
            new_message += letter
    print(new_message)

