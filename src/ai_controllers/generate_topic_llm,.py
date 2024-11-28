#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:09:24 2024

@author: krishnayadav
"""

import json
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from telegram import *
from langchain_community.llms import Ollama


embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
llm = Ollama(model="mistral", temperature=1)   

def get_cleaned_topic(response):
    if '.' in response:
        return response.split(".")[1]

def generate_topic_BERT():
    chat_messages = get_last_100_message('polk_gov')
    chat_messages = [msg for msg in chat_messages if len(msg.split()) > 2]
    topic_model = BERTopic(embedding_model=embedding_model, min_topic_size=2)
    topics, probs = topic_model.fit_transform(chat_messages)
    
    topic_list = []
    for topic_id, topic in topic_model.get_topics().items():
        if topic_id != -1:  # Exclude outliers
            topic_list.append(" ".join([word for word, _ in topic]))
    
    conversations = []
    length_topic = 5 if len(topic_list) > 5 else len(topic_list)
    
    for topic in topic_list[:length_topic]:
        # Create a dynamic prompt for each topic
        prompt = f"""
        Topic: "{topic}"
        generate me a list of topic from above conversation in list
        """
        # Get the response from the model
        response = llm.invoke(prompt, max_tokens=200,  temperature=0.7, stop = ["\n"])  
        cleaned_response = get_cleaned_topic(response)
        print(response)
        print(cleaned_response)
        print("------------")
        conversations.append(response)
    
    
    
    
    
    