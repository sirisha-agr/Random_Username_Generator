import random
import string
adjective = ["bright", "cheerful", "brilliant", "calm", "brave", "elegant", "gentle", "hasty", "quick", "shiny"]
noun = ["apple", "ocean", "mountain", "river", "cloud", "forest", "star", "flower", "stone", "bird"]
digit = list(range(10))
special_char = list(string.punctuation)
is_running = True
usernames = []
print("Hello, welcome to username generator!")
print("-------------------------------------------------------------------------------------------------------------------------------------")
def generate_username():
    user = random.choice(adjective) + random.choice(noun)
    choice = input("Do you want to include a special character or digit? (Y/N) ").upper()
    if choice == 'Y':
        ch1 = input("Digit or Special Character? ").lower()
        if ch1 == 'digit':
            user += str(random.choice(digit))
        elif ch1 == 'special character':
            user += random.choice(special_char)
    return user
while is_running:
    user = generate_username()
    usernames.append(user)
    print("The username is:", user)
    choose = input("Do you want to continue generating usernames? (Y/N) ").upper()
    if choose == 'N':
        is_running = False
    elif choose != 'Y':
        print("Invalid Value")
    
with open('text.txt', 'a') as file:
    for username in usernames:
        file.write(username + "\n")

print("-----THANK YOU------")
    

        

    
        
    
      
