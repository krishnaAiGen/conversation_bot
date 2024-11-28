import os
from datetime import datetime, timedelta
import pickle
from utils import *
import json

with open('config.json', 'r') as json_file:
    config = json.load(json_file)

def get_message():
    message = "Good morning guys. Donald J trump won the election. What do you think it's impact on Crypto market?"
    
    return message

def store_initiate_conversation(conversations_dict):
    time_persona_dict = {}
    description_list = []
    now = datetime.now()
    # current_time = now.strftime("%H:%M")

    for key, value in conversations_dict.items():
        for key1, value1 in value.items():

            new_time = now + timedelta(minutes=key1)
            new_time_str = new_time.strftime("%H:%M")
            time_persona_dict[new_time_str] = key
            description_list.append(value1)
            
            now = new_time
    
    save_dictionary(time_persona_dict, config['data_dir'])
    save_list(description_list, config['data_dir'])

    print("Initiate conversation data saved successfully!")  
    

def send_to_telegram(persona, reply):
    # send_to_telegram()
    
    print(reply, "sent to telegram")


def conversation_initiate_status():
    # react_status, inititate_status = conversation_initiate_telegram()
    
    #Logic is like this
    """
    If there is any last conversation and whose reply is not given, then it's a reaction chat, on time 1 hr,
    give it's reply. 
    
    Initiation status, if init
    """
    
    
    """
    this is for initiation_send_status
    """
    
    time_persona_dict = load_dictionary(config['data_dir'])
    if len(time_persona_dict) == 0:
        initiation_send_status = False
    
    else:
        initiation_send_status = True
        
    
    """
    this is for conversation inititation stattus
    checking two condition, if conversation dict is empty and last time is > treshold time,
    then conversation_initiation status is True
    """
    
    
    
    """
    For react status, get a distribution from 0 to 9, if integer equals to 2 and 5 then only send react status
    """
    
    
    """
    send_random_message_status. If there is no talk in last 1 day, then send some random message.
    """
    
    

    
   
    return react_status, inititate_status, initiation_send_status

def create_db(directory, filename="discussed_topic.json"):
    # Construct the full path to the file
    file_path = os.path.join(directory, filename)

    # Check if the file exists
    if not os.path.exists(file_path):
        # Create the file with an empty dictionary
        with open(file_path, 'w') as file:
            file.write('{}')  # Creates an empty JSON dictionary
        print(f"File '{filename}' created in '{directory}'.")
    else:
        print(f"File '{filename}' already exists in '{directory}'.")

def send_initiation_chat():
    time_persona_dict = load_dictionary(config['data_dir'])
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    
    current_time = '14:39'
    
    if len(time_persona_dict) == 0:
        return 
    
    else:
        counter = 0
        for key, value in time_persona_dict.items():
            if key == current_time:
                discussion_list = load_list(config['data_dir'])
                send_to_telegram(value, discussion_list[counter])
                del time_persona_dict[key]
                discussion_list.pop(counter)
                
                save_dictionary(time_persona_dict, config['data_dir'])
                save_list(discussion_list, config['data_dir'])

            counter = counter + 1
        
        

    
    
    