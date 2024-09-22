# questions.py

import win32com.client as win
speaker = win.Dispatch("SAPI.SpVoice")

def question1(money, index=None):
    question = "What was the name of the first Prime Minister of India?"
    answers = ["M.K Gandhi", "Jawaharlal Nehru", "Mukesh Ambani", "None of the above"]
    if index is not None:
        speaker.speak(f"You have chosen option {index+1}.")
        if index == 1:
            return True
        else:
            return False
    return question, answers

def question2(money, index=None):
    question = "Who holds the record of having the most number of centuries in ODIs?"
    answers = ["Sachin Tendulkar", "Ricky Ponting", "Virat Kohli", "Brian Lara"]
    if index is not None:
        speaker.speak(f"You have chosen option {index+1}.")
        if index == 2:
            return True
        else:
            return False
    return question, answers

def question3(money, index=None):
    question = "Who sings The National Anthem at Red Fort on Independence Day?"
    answers = ["The Prime Minister", "The President", "The Chief Minister", "None of the above"]
    if index is not None:
        speaker.speak(f"You have chosen option {index+1}.")
        if index == 0:
            return True
        else:
            return False
    return question, answers

def question4(money, index=None):
    question = "COVID-19 outbreak started from which City of the World?"
    answers = ["Wuhan, China", "NYC, America", "Kolkata, India", "Antipolo, Philippines"]
    if index is not None:
        speaker.speak(f"You have chosen option {index+1}.")
        if index == 0:
            return True
        else:
            return False
    return question, answers

def question5(money, index=None):
    question = "Who holds the record of having the most number of centuries in International Cricket?"
    answers = ["Sachin Tendulkar", "Ricky Ponting", "Virat Kohli", "Brian Lara"]
    if index is not None:
        speaker.speak(f"You have chosen option {index+1}.")
        if index == 0:
            return True
        else:
            return False
    return question, answers

def question6(money, index=None):
    question = "Who is the first IAS officer in India?"
    answers = ["M. A. Sreenivasan", "C. Rajagopalachari", "Satyendranath Tagore", "Lakshmikant Prasad"]
    if index is not None:
        speaker.speak(f"You have chosen option {index+1}.")
        if index == 2:
            return True
        else:
            return False
    return question, answers

def question7(money, index=None):
    question = "Which of these is the other name of Harappan Civilisation?"
    answers = ["Aryan Civilisation", "Indus Valley Civilization", "Vedic Civilization", "All Of these"]
    if index is not None:
        speaker.speak(f"You have chosen option {index+1}.")
        if index == 1:
            return True
        else:
            return False
    return question, answers

def question8(money, index=None):
    question = "What is the name of our Father of Nation?"
    answers = ["M.K Gandhi", "Jawaharlal Nehru", "Mukesh Ambani", "None of the above"]
    if index is not None:
        speaker.speak(f"You have chosen option {index+1}.")
        if index == 0:
            return True
        else:
            return False
    return question, answers

def question9(money, index=None):
    question = "Who holds the record of having the most number of Double centuries in ODIs?"
    answers = ["Sachin Tendulkar", "Ricky Ponting", "Rohit Sharma", "Brian Lara"]
    if index is not None:
        speaker.speak(f"You have chosen option {index+1}.")
        if index == 2:
            return True
        else:
            return False
    return question, answers

def question10(money, index=None):
    question = "Which of these is the feature of Harappan Civilisation?"
    answers = ["Urban Planning", "Drainage System", "Upper citadel and Lower city", "All of the above"]
    if index is not None:
        speaker.speak(f"You have chosen option {index+1}.")
        if index == 3:
            return True
        else:
            return False
    return question, answers
