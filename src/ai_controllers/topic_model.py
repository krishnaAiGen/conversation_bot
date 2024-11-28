#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 16:31:49 2024

@author: krishnayadav
"""

import json
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer



# Specify the path to your JSON file
file_path = '/Users/krishnayadav/Downloads/random_messages.json'

# Load JSON data from the file
with open(file_path, 'r') as file:
    data = json.load(file)



chat_list = []
for key, value in data.items():
    content = value['content']
    for dict2 in content:
        chat_list.append(dict2['message'])
        

chat_messages = chat_list[:100]    

# Preprocess chat messages (remove short/empty messages)
chat_messages = [msg for msg in chat_messages if len(msg.split()) > 2]

# Load a pre-trained embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize BERTopic with the custom embedding model
topic_model = BERTopic(embedding_model=embedding_model, min_topic_size=2)

# Fit the model to the chat messages
topics, probs = topic_model.fit_transform(chat_messages)

# Display topics
print("Generated Topics:")
for topic_id, topic in topic_model.get_topics().items():
    if topic_id != -1:  # -1 represents outliers
        print(f"Topic {topic_id}: {[word for word, _ in topic]}")



topic_list = []

# Extract topics and append to the list
for topic_id, topic in topic_model.get_topics().items():
    if topic_id != -1:  # Exclude outliers
        # Join topic words with space and add to the list
        topic_list.append(" ".join([word for word, _ in topic]))

# Print the list of topics
print("List of Topics:")
print(topic_list)



from langchain_community.llms import Ollama
llm = Ollama(model="mistral", temperature=1)   


conversations = []

def get_cleaned_topic(response):
    if '.' in response:
        return response.split(".")[1]
    

# for topic in topic_list[:5]:
    topic = ''.join(chat_messages)
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
    




    
    

