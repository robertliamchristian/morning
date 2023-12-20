import datetime
import requests
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import random
import datetime
from datetime import datetime as dt

def get_random_food():
    breakfast_options = ["protein shake", "protein bar"]
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
    task_options = ["clean litter", "walk", "meditate", "yoga", "play guitar", "call a friend", "send Lindsay flowers"]
    
    return {
        'task': random.choice(task_options)
    }

def get_random_affirmation():
    affirmations = [
        "I am healing my body with each deep breath.",
        "My body is healthy and strong.",
        "My body is powerful and knows how to heal itself.",
        "My positive thoughts and actions renew my health and body.",
        "I deserve to feel healthy and vibrant.",
        "It feels good to take care of myself.",
        "My body can do amazing things.",
        "Things are always working in my favor.",
        "I am nice to my body.",
        "Resting my body is my birthright.",
        "My body is sacred and I will take care of it.",
        "I exercise to honor my body’s strength.",
        "I am kind to my body.",
        "My body is perfect the way it is.",
        "I am healthy, optimistic, and happy.",
        "I am grateful for my life force.",
        "My immune system is strong and keeps me safe.",
        "I trust my body to know what it needs, and I listen.",
        "I eat food to nourish and celebrate my body.",
        "I sleep soundly and peacefully."
    ]

    selected_affirmation = random.choice(affirmations)
    return selected_affirmation


