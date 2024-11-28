#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 20:30:13 2024

@author: krishnayadav
"""

from sentence_transformers import SentenceTransformer, util
from llm_personas import get_human_reply, get_crypto_reply, get_persona_type, refine_reply
from classify_chat import ClassifyChat
from langchain_community.llms import Ollama
import time
from telegram_scanner import *
from initiate_topic import *
import json
import random
from generate_topic_llm import *

with open('config.json', 'r') as json_file:
    config = json.load(json_file)
    
cred = credentials.Certificate(config["firebase_cred"])
app = firebase_admin.initialize_app(cred)
db = firestore.client()

def telegram_react():
    #hit prince api
    # message = get_message()
    message_type, human_crypto_score = classify_human_blockchain.predict(message)
    if message_type == 'human':
        human_reply = get_human_reply(message, llm)
        
        return human_reply
    else:
        persona = get_persona_type(message, sim_model)
        crypto_reply = get_crypto_reply(message, llm, persona)
        crypto_reply = refine_reply(crypto_reply)
        
        return crypto_reply

def initiate_bot_conversation():
    #get topic from crypto topic list 
    topic_list = get_topic_llm(db)
    topic = topic_list[0]
    topic_status = get_topic_status(topic)
    
    while not topic_status:
        topic = get_topic(llm, topic_model)
        topic_status = get_topic_status(topic)
    
    #get topic from external hot topic
    save_topic_to_db(topic)
    
    conversations_dict = get_bot_conversation(topic, sim_model, llm)
    
    #only for blobsubscriptions delete for other
    persona = get_persona_question(conversations_dict)
    # send_to_telegram(persona, topic)
    
    store_initiate_conversation(conversations_dict)
    
    return conversations_dict

def close_firebase_client(app):
    firebase_admin.delete_app(app)
    print("Firebase client closed successfully.")
        


if __name__ == "__main__":
    global sim_model
    sim_model = SentenceTransformer('all-MiniLM-L6-v2')  # You can choose another model if preferred
    classify_human_blockchain = ClassifyChat(config['chat_classify'])
    
    global llm 
    llm = Ollama(model="llama2-uncensored", temperature=0.9)
    
    create_db(config['data_dir'])
    
    while True:
        try:
            # react_status, initation_status, initiation_send_status, send_random_status = conversation_initiate_status()
            
            initation_status = True
            react_status = False
            initiation_send_status = True
            
            if react_status:
                reply = telegram_react()
                send_to_telegram(reply)
                react_status = False
            
            if initation_status:
                reply = initiate_bot_conversation()  
                initation_status = False
            
            if initiation_send_status:
                send_initiation_chat()
            
            if send_random_message_status:
                send_random_talks()
            
        except Exception as e:
            print("--------error occured-------", e)
        
        finally:
            try:
                close_firebase_client(app)
            except:
                continue
            
            







