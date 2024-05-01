'''
Develop elementary chat bot for suggesting investment as
per the customer needs.
'''
import random

language={
    "greet":["hi","hello","how are You?"],
    "response_greet":["hi,i am chatbot!","hello,how can i help you?","how are you?"],
    "bye":["goodbye","bye"],
    "response_bye":["bye have a good day!","goodbye,hope to see you soon!"],
    "default":["Sorry,I dont have a answer to your question."],
    "card":["How do I report a lost or stolen card?"],
    "response_card":["Call our customer service hotline immediately to report it."],
    "account":["How do I open a new account?"],
    "response_account":["Visit our website and follow the prompts to apply online."],
    "loan":["How do I apply for a loan?"],
    "response_loan":["Fill out our online loan application form on our website."],
    "balance":["What's my current account balance?"],
    "response_balance":["Log in to your online banking account or use our mobile app to check your balance."]
}

def getUserInput():
    return input("You : ")

def getResponse(userInput):
    for type in language:
       # print(type)
        for sentence in language[type]:
            if userInput.lower()==sentence.lower():
                return language["response_"+type]
    return language["default"]

print("Hi I am ChatBot!")

while True:
    userInput=getUserInput()
    botResponse=getResponse(userInput)
    print("ChatBot : "+random.choice(botResponse))
    if botResponse==language["response_bye"]:
        break
