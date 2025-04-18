# simple chatbot in python

print("Hello! I am ChatBot. Type 'bye' to exit." )

while True:
    user_input = input("You: ").lower() # lower() makes the input lowercase (so it works even if the user types "HELLO")

    if user_input == "hello" :
        print("Bot: Hi there!")
    elif user_input == "how are you" :
        print("Bot: I am just a bunch of code, but thanks for asking")
    elif user_input == "what is your name?":
        print("Bot: I am ChatBot. Your friendly Python bot.")
    elif user_input == "bye" : 
        print("Bot: See you later")
        break  # break ends the loop if the user says "bye"
    else:
        print("Bot: Sorry, I did not understand that.")
