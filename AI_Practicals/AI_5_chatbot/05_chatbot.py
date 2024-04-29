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
    "weather":["How is the weather?"],
    "response_weather":["The weather today is sunny.","The weather today is rainy.","The weather today is cloudy."]
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
