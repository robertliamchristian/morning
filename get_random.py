import datetime
import requests
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import random
import datetime
from datetime import datetime as dt

def get_random_food():
    breakfast_options = ["protein shake"]
    lunch_options = ["Paris Baguette", "Subway", "sushi"]
    dinner_options = ["Paris Baguette", "Subway", "sushi", "Mexican", "fast food"]
    
    return {
        'breakfast': random.choice(breakfast_options),
        'lunch': random.choice(lunch_options),
        'dinner': random.choice(dinner_options)
    }

def get_random_turkish_quote():
    quotes = [
        ("Damlaya damlaya göl olur.", "Drop by drop, it becomes a lake."),
        ("Bir elin nesi var, iki elin sesi var.", "One hand has a limited ability, but two hands clap."),
        ("Bir musibet bin nasihatten iyidir.", "One calamity is better than a thousand pieces of advice."),
        ("Aç kurt bile komşusunu yemez.", "Even a hungry wolf won’t eat its neighbor."),
        ("Balık baştan kokar.", "The fish stinks from the head."),
        ("Atın ölümü arpadan olsun.", "Let the horse die from too much barley."),
        ("Değirmenin suyu nereden geliyor?", "Where does the mill’s water come from?"),
        ("Gülü seven dikenine katlanır.", "Who loves a rose will endure its thorns."),
        ("Küçükken damlayan yağmur, büyüyünce sel olur.", "The rain that drips when it's small, becomes a flood when it grows."),
        ("Kedi uzanamadığı ciğere mundar der.", "The cat calls the liver it can't reach rotten.")
    ]

    selected_quote = random.choice(quotes)
    return selected_quote

def get_random_tasks():
    task_options = ["clean litter", 
                    "walk", 
                    "meditate", 
                    "yoga", 
                    "play guitar", 
                    "call a friend", 
                    "send Lindsay flowers"
                    
                    ]
    
    return {
        'task': random.choice(task_options)
    }

def get_random_affirmation():
    affirmations = [
        "My body is powerful and knows how to heal itself.",
        "My positive thoughts and actions renew my health and body.",
        "I deserve to feel healthy and vibrant.",
        "It feels good to take care of myself.",
        "My body can do amazing things.",
        "Things are always working in my favor.",
        "Resting my body is my birthright.",
        "My body is perfect the way it is.",
        "My immune system is strong and keeps me safe.",
        "I trust my body to know what it needs, and I listen.",
        #mine
        "I can lose weight and feel young again",
        "I am strong and healthy",
        "I am in control of my health",
        "My cats are happy and healthy",
        "My partner loves me and likes who I am",
        "I am a good person",
        "I am a good son and brother",
        "I have accomplished a lot of things and will accomplish many more things",
    ]

    selected_affirmation = random.choice(affirmations)
    return selected_affirmation

'''

"







'''
