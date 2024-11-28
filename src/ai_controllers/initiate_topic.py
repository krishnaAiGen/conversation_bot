import random
import json
from llm_personas import get_persona_type
import numpy as np
from datetime import datetime
from utils import * 


with open('prompt.json', 'r') as json_file:
    personas = json.load(json_file)

with open('personas.json', 'r') as json_file:
    personas_index = json.load(json_file)
    
with open('config.json', 'r') as json_file:
    config = json.load(json_file)

def conversation_to_topic(llm, chat, topic_model):    
    message = personas['generate_topic'] + '"' + chat + '"'
    topic_reply = llm.invoke(message)
    topic, prob = topic_model.transform(topic_reply)
    topics = topic_model.topic_labels_[topic[0]].split('_')[1:]
    topic_selected = topics[random.randint(0, len(topics) - 1)]
    
    return topic_selected


def get_topic_list(llm, topic_model):
    previous_chat = get_chat() #extract previous 30 days chat
    topic = conversation_to_topic(llm, previous_chat, topic_model)
    
def read_topic_list(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data_list = [line.strip() for line in file]  # Read lines and strip whitespace
        return data_list
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
def get_persona_question(conversations_dict):
    dict_keys = conversations_dict.keys()
    while True:
        random_persona = personas_index[str(random.randint(0, 9))]
        if random_persona not in dict_keys:
            break
    
    return random_persona
    

def get_bot_conversation(topic, sim_model, llm):
    conversations_dict = {}
    
    persona = get_persona_type(topic, sim_model)
    persona_template = personas[persona]
    # message = persona_template + " " + "What do you think about " + topic + "in crypto market. Write in 50 words"
    message = persona_template + " " + topic + "Write within 50 words"
    persona_reply = llm.invoke(message)
    
    time = random.randint(5, 60)
    conversations_dict[persona] = {time : persona_reply}
    
    number_of_bot_involved = random.randint(2, 10)
    bot_index = np.random.randint(0, 10, size=number_of_bot_involved)
    bot_index = list(set(bot_index))
    first_bot_index = next(key for key, value in personas_index.items() if value == persona)
    
    
    for index in bot_index:
        print(index, " generating conversation...")
        if index == int(first_bot_index):
            continue
        
        persona = personas_index[str(index)]
        
        persona_template = personas[persona]
        message = persona_template + " " + "What do you think about " + topic + "in crypto market. Write in 50 words"
        persona_reply = llm.invoke(message)
        time = random.randint(5, 60)

        conversations_dict[persona] = {time : persona_reply}
    
    return conversations_dict

def load_topic_db(key_value_status):
    with open(config['data_dir'] + 'discussed_topic.json', 'r') as json_file:
        discussed_topic = json.load(json_file)
    
    if key_value_status == False:
        discussed_topic = list(discussed_topic.values())
    
    return discussed_topic

def get_topic_status(topic):
    discussed_topic = load_topic_db(False)
    
    if topic not in discussed_topic:
        return True
        
    else:
        return False
    
def save_topic_to_db(topic):
    discussed_topic = load_topic_db(True)
    current_timestamp = datetime.now()
    
    discussed_topic[str(current_timestamp)] = topic
    
    with open(config['data_dir'] + 'discussed_topic.json', 'w', encoding='utf-8') as json_file:
        json.dump(discussed_topic, json_file, indent=4)  # Use indent for pretty
    
    print(f'saved {topic} to the discussed topic successfully')
    

def send_random_talks():
    random_message = read_topic_list(config['data_dir'] + 'random_message.txt')
    
    random
    
    
        
# get_chat(time):
#     call_to
    
#     send_chat(persona, message)


        
    
    
    
    









    