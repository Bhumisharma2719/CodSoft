#import random so that the password occur randomly
import random
import string
#taking user input of lengh
length = int(input ("Specify the length of password you want: "))
#defining function for generating password
def generate_pass(length):
    #password having punctuations, digits , uppercase(A-Z) and lowercase(a-z)
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    #join random choices in length range
    password = ''.join(random.choice(characters) for i in range(length))
    return password
print("GENERATED PASSWORD : ", generate_pass(length))