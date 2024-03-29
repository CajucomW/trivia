import requests
import random
from django.shortcuts import render

response = requests.get('https://opentdb.com/api.php?amount=10')
data = response.json()
user_answer = None

correct_list = []
# def welcome():

#     print("Welcome to Our Group Project!")
#     username = input("Please enter a Username: ")
    
# welcome()

def quiz():
    # while True:
    for item in data['results']:            # get to the right list
        print(item['question'])
        correct = item['correct_answer']    # reference keys for correct answers
        choices = item['incorrect_answers'] # reverence keys for incorrect answers
        
        answers = []
        for choice in choices:
            answers.append(choice)      # this adds the wrong answers to the list "answers"
        answers.append(correct)         # this adds the right answer to he list "answers"
        random.shuffle(answers)         # this randomizes all the answers from the list "answers"
        
        print(answers)
        
        user_answer = input("Type your answer here: ")
        if user_answer in correct:
            correct_list.append(user_answer)
            print("You got it!")
        else:
            print("Sorry. The answer is", correct + ".")
        
        print(correct_list)

def scores():
    correct_number = 0
    correct_number = len(correct_list)
    score = correct_number * 10
    print("You scored", score, "%")

quiz()

scores()