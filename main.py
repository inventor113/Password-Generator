import random

class PASSWORD:
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                        'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 
                        'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', 
                        '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', 
                        '{', '}', ';', ':', ',', '.', '<', '>', '/', '?', '|', '~']

    def create(self):
        
        self.i = int(input("Length of your password: "))
        
        
        password = ''.join(random.choice(self.letters) for _ in range(self.i))
        
        
        print(f"Here's your password: {password}")


password_generator = PASSWORD()
password_generator.create()
