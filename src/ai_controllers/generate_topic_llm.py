#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:09:24 2024

@author: krishnayadav
"""

import json
from sentence_transformers import SentenceTransformer
from telegram import *
from langchain_community.llms import Ollama
import re
from openai_chat import get_llm_response


# embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
# llm = Ollama(model="mistral", temperature=1)   

# def get_cleaned_topic(response):
#     if '.' in response:
#         return response.split(".")[1]

# def generate_topic_BERT(db):
#     chat_messages = get_last_100_message('polk_gov', db)
#     chat_messages = [msg for msg in chat_messages if len(msg.split()) > 2]
    
    
#     topic_model = BERTopic(embedding_model=embedding_model, min_topic_size=2)
#     topics, probs = topic_model.fit_transform(chat_messages)
    
#     topic_list_bert = []
#     for topic_id, topic in topic_model.get_topics().items():
#         if topic_id != -1:  # Exclude outliers
#             topic_list_bert.append(" ".join([word for word, _ in topic]))
    
#     topic = ''.join(topic_list_bert)
#     prompt = f"""
#     Topic: "{topic}"
#     Extract five numbered list of key topics discussed from above chat. Each topic should be concise and directly relevant.
#     """
#     topics = []
    
#     while len(topics) <= 0: 
#         print("iteration...")
#         response = llm.invoke(prompt, temperature=1) 
#         topics = re.findall(r'\d+\.\s*(.*)', response)
    
    
#     return topics        
    
# def get_topic_llm(db):
#     topic_list_llm = generate_topic_BERT(db)
    
#     return topic_list_llm

def get_topic_llm(db):
    chat_messages = get_last_100_message('polk_gov', db)
    chat_messages = [msg for msg in chat_messages if len(msg.split()) > 2]
    chat_messages_join = ''.join(chat_messages)
    
    content  = f"""
    #     Topic: "{chat_messages_join}"
    #     Extract five numbered list of key topics discussed from above chat. Each topic should be concise and directly relevant.
    #     """
    
    topics = []
    while len(topics) <= 0: 
            print("iteration...")
            response = get_llm_response(content)
            topics = re.findall(r'\d+\.\s*(.*)', response)    
            
    return topics
    
    
    
    