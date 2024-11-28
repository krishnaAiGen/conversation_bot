#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 12:06:18 2024

@author: krishnayadav
"""

from telethon import TelegramClient, events
import os
import json
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore
from google.api_core.retry import Retry


load_dotenv()

def get_last_100_message(collection_name, db):
    sanitized_name = collection_name.lstrip('@')
    final_name = f"conversation_ai_{sanitized_name}"
    collection_ref = db.collection(final_name)
    
    data_list = []
    docs = collection_ref.stream()
    for doc in docs:
        doc_data = doc.to_dict()  # Convert the document snapshot to a dictionary
        data_list.append(doc_data)  # Append the data to the list
    
    message_list = []
    for dict1 in data_list[:100]:
        message_list.append(dict1['text'])
    
    return message_list


# USERS = {
#     "Me0_0Prince": {
#         "api_id": 20699916,
#         "api_hash": "f128d1f226e394b87c437970c9a6f483",
#         "username": "Me0_0Prince",
#         "phone_no": "+918054984350"
#     }
# }

# CHANNEL_USERNAME = "@polk_gov"

# clients = {}
# for user, config in USERS.items():
#     clients[user] = TelegramClient(config["username"], config["api_id"], config["api_hash"])



# async def fetch_and_save_channel_messages(client, channel_username):
#     await client.start()
#     print(f"Fetching all messages from {channel_username}")
#     collection = get_collection(channel_username)

#     # Initialize Firestore batch
#     batch = db.batch()
#     batch_count = 0  # Keep track of the number of operations in the current batch
#     total_count = 0  # Total number of messages processed

#     async for message in client.iter_messages(channel_username):
#         if message.text:
#             doc_ref = collection.document(str(message.id))  # Reference to the document
#             doc_data = {
#                 "message_id": message.id,
#                 "text": message.text,
#                 "sender_id": message.sender_id,
#                 "date": message.date  # Firestore handles datetime.datetime objects
#             }
#             batch.set(doc_ref, doc_data)  # Add the operation to the batch
#             batch_count += 1
#             total_count += 1

#             # Commit the batch if the limit is reached
#             if batch_count == 500:
#                 batch.commit()  # Commit the batch to Firestore
#                 print(f"Committed 500 messages to Firestore.")
#                 batch = db.batch()  # Start a new batch
#                 batch_count = 0

#     # Commit any remaining operations in the batch
#     if batch_count > 0:
#         batch.commit()
#         print(f"Committed the final {batch_count} messages to Firestore.")

#     print(f"Total messages saved: {total_count}")


# async def send_message_from_user(user, message):
#     if user not in clients:
#         print(f"User {user} not found!")
#         return

#     client = clients[user]
#     async with client:
#         await client.send_message(CHANNEL_USERNAME, message)
#         print(f"Message sent to {CHANNEL_USERNAME} by {user}: {message}")

# async def listen_to_channel_messages():
#     listening_client = list(clients.values())[0]
#     async with listening_client:
#         @listening_client.on(events.NewMessage(chats=[CHANNEL_USERNAME]))
#         async def handle_new_message(event):
#             print(f"New message in {CHANNEL_USERNAME}: {event.raw_text}")
#             collection = get_collection(CHANNEL_USERNAME)
#             doc_data = {
#                 "message_id": event.id,
#                 "text": event.raw_text,
#                 "sender_id": event.sender_id,
#                 "date": event.date
#             }
#             collection.document(str(event.id)).set(doc_data)
#             print(f"Saved new message: {doc_data}")

#         print(f"Listening for new messages in {CHANNEL_USERNAME}...")
#         await listening_client.run_until_disconnected()

# async def main():
#     await send_message_from_user("Me0_0Prince", "Hello!")
#     # await fetch_and_save_channel_messages(clients["Me0_0Prince"], CHANNEL_USERNAME)
#     # await listen_to_channel_messages()

# if __name__ == "__main__":
#     import asyncio

#     asyncio.run(main())