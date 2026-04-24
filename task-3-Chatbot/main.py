def reply(user):
    if user == "hello":
        return "Hello! How can I hlep you?"

    elif user == "how are you?":
        return "I am fine, thanks!"

    elif user == "your name":
        return "I am a simple cahtbot"

    elif user == "bye":
        return "Goodbye!" 

    else:
        return "I don't understand"              

while True:
    user = input("You: ").lower()

    response = reply(user)
    print("Bot: ",response)

    if user == "bye":
        break