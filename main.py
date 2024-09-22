import tkinter as tk
import win32com.client as win
import time
import pygame
import random
from questions import *

speaker = win.Dispatch("SAPI.SpVoice")

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

def abc():
    clap()
    time.sleep(1)
    speaker.speak("Let's move to the next question")
    time.sleep(1)

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

def clap():
    audio_file = r"D:\applause-2.mp3" 
    play_audio(audio_file)

def speak_text(text):
    speaker.speak(text)

def display_question(game_state, question_functions):
    if game_state['current_question_index'] < len(question_functions):
        question_func = question_functions[game_state['current_question_index']]

    question, answers = question_func(game_state['money'], None)
    
    # Speak the question
    speak_text(question)
    
    # Update the GUI
    root.question_label.config(text=question)
    for i, answer in enumerate(answers):
        root.answer_buttons[i].config(text=answer)
    
    # Speak options after a short delay
    root.after(1000, speak_options, answers)

def speak_options(answers):
    for i, answer in enumerate(answers):
        speak_text(f"Option {i+1}: {answer}")
        time.sleep(0.5)  # Add a small delay between speaking options

def check_answer(game_state, question_functions, index):
    if game_state['current_question_index'] < len(question_functions):
        question_func = question_functions[game_state['current_question_index']]

    correct_answer = question_func(game_state['money'], index)
    
    if correct_answer:
        # Increment correct answers count
        game_state['correct_answers_count'] += 1
        
        # Fetch the money based on correct answers count
        prize_money = game_state['money'][game_state['correct_answers_count'] - 1]
        
        result_text = f"Correct! You won Rs. {prize_money}."
        root.output_label.config(text=result_text)
        speak_text(result_text)
        game_state['Your_Prize'] = prize_money
        abc()
    else:
        result_text = "Wrong answer. You lost."
        root.output_label.config(text=result_text)
        speak_text(result_text)
        print(Color.RED + "You lost" + Color.RESET)
        print(f"You drop down to Rs. {game_state['Your_Prize']}")
        root.after(2000, root.destroy)  # Close the GUI after 2 seconds
        return

    game_state['current_question_index'] += 1
    if game_state['current_question_index'] < len(question_functions):
        root.after(2000, display_question, game_state, question_functions)
    else:
        final_message = f"Congratulations! You won Rs. {game_state['Your_Prize']}."
        root.output_label.config(text=final_message)
        speak_text(final_message)

root = tk.Tk()
root.title("Quiz Game")
root.geometry("800x500")
root.configure(bg='#73AFDD')

# Randomizing questions
question_functions = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10]
random.shuffle(question_functions)

game_state = {
    'money': [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000],
    'Your_Prize': 0,
    'current_question_index': 0,
    'correct_answers_count': 0
}

name_label = tk.Label(root, text="Enter your name:")
name_entry = tk.Entry(root)
start_button = tk.Button(root, text="Start", command=lambda: start_quiz(question_functions, name_entry.get()))

root.question_label = tk.Label(root, text="", font=("Arial", 16),bg='#D3D3D3')
root.output_label = tk.Label(root, text="", font=("Arial", 16),bg='#D3D3D3')
root.answer_buttons = [tk.Button(root, text=f"Option {i+1}", command=lambda i=i: check_answer(game_state, question_functions, i)) for i in range(4)]

name_label.pack(pady=10)
name_entry.pack(pady=10)
start_button.pack(pady=20)
root.question_label.pack(pady=10)
root.output_label.pack(pady=10)
for button in root.answer_buttons:
    button.pack(pady=5)

def start_quiz(question_functions, name):
    speak_text(f"Welcome to the game, {name}. Let's start!")
    display_question(game_state, question_functions)

root.mainloop()
