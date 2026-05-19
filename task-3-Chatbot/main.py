def reply(user):
    if user == "hello":   # here I use predefined chats to reply to the user
        return "Hello! How can I hlep you?"

    elif user == "how are you?":
        return "I am fine, thanks!"

    elif user == "your name":
        return "I am a simple cahtbot"

    elif user == "bye":
        return "Goodbye!" 

    else:
        return "I don't understand"     # if the user input is not in the predefined chats, it will reply with this message         

while True:
    user = input("You: ").lower()

    response = reply(user)
    print("Bot: ",response)

    if user == "bye":
        break