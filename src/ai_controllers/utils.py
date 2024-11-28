import pickle
import json

def save_dictionary(dictionary, filename):        
    with open(filename + 'time_persona.json', 'w', encoding='utf-8') as json_file:
        json.dump(dictionary, json_file, indent=4)  # Use indent for pretty

def load_dictionary(filename):
    with open(filename + 'time_persona.json', 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

def save_list(lst, filename):
    filename = filename + 'discussion.txt'
    with open(filename, 'wb') as file:
        pickle.dump(lst, file)

def load_list(filename):
    filename = filename + 'discussion.txt'
    with open(filename, 'rb') as file:
        return pickle.load(file)
    
