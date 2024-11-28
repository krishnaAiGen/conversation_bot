#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 11:28:35 2024

@author: krishnayadav
"""
import json

topic_list = [
"Morning, Blob fam! Who's got eyes on the latest subscription alpha? 📈",
"Blob warriors, rise and grind! 🚀 Any new tokens you’re watching today?",
"GM Blobbers! Any hidden gems you found overnight? Let’s keep the hype rolling!",
"What’s the vibe today, team? Bullish or bearish on BlobSubscriptions?",
"Who’s HODLing strong today? 💎 Drop your most promising subscriptions!",
"What’s everyone aping into today on BlobSubscriptions? Share the hype! 🐒",
"Good morning, Blob fam! 🌅 What’s on your watchlist today?",
"Any new projects we should ape into on Blob? 🐵 Drop your finds!",
"How’s everyone feeling today? Any juicy updates from BlobSubscriptions?",
"Who’s ready to take their subs to the next level? 🚀 Share your thoughts!",
"Hey, Blobbers! Any projects gaining traction on your radar?",
"Morning, everyone! Let’s hear those alpha predictions for today!",
"Who’s scouting for new NFTs on Blob today? 🎨 Let’s keep the chat buzzing!",
"Any fresh signals today? 📡 Let’s make some noise in the Blob space!",
"What’s popping today? 💥 Which subs are you backing?",
"Any hot tips for Blob projects that are about to moon? 🌙",
"WAGMI, Blob fam! Who’s bullish on today’s offerings?",
"Which coins on Blob are worth a closer look today? 👀",
"Hey, everyone! Any new BUIDLing projects that caught your eye? 🛠️",
"Let’s talk subs! Anyone got inside intel on today’s top listings?",
"What’s the sentiment today, Blob gang? 🚀 Bearish or bullish?",
"GM fam! Any airdrops happening today on Blob?",
"Time to discuss the sleeper projects on Blob! Who’s got the inside scoop?",
"Blob fam, let’s drop our hottest picks of the day! 🔥",
"Ready to ride some waves today? 🌊 Which projects have your interest?",
"Checking in! Who’s all-in on the latest listings?",
"Who’s HODLing strong through the market swings today? 💪",
"Morning, Blob fam! What’s trending today in the subscription space?",
"Any fresh ICOs or IDOs on Blob worth looking at today? 🌐",
"Who’s got their diamond hands on a promising project today? 💎",
"Hey Blob fam! Who’s joining the FOMO train today? 🚂",
"What’s the top signal on Blob today? Share your alpha!",
"Hope everyone’s stacking sats! What’s hot on Blob today?",
"What are your favorite sleeper tokens on Blob? 💤",
"How’s everyone feeling? Ready to ride another bullish wave?",
"What’s on the radar for Blob fam today? Let’s keep the chat alive!",
"Any new projects that scream moonshot today? 🌕 Let’s discuss!",
"Morning vibes! What’s everyone’s top pick on Blob today?",
"Calling all Blob degens! 🤑 Which projects are worth checking out?",
"How’s everyone doing? Found any promising airdrops on Blob lately?",
"Which projects are you aping into today on Blob? 🐒",
"GM Blobbers! Let’s make today’s chat legendary with alpha insights!",
"How’s everyone BUIDLing today? Got any subscription gems to share?",
"Morning fam! What’s everyone’s thoughts on today’s projects?",
"Let’s talk potential moonshots today! Which projects stand out?",
"Ready for a new day of gains, Blob fam? Drop your insights!",
"What’s the FOMO level today on Blob? 🔥 Let’s stay connected!",
"Rise and shine! Any new listings catching your eye today?",
"Who’s ready to stack those sats on Blob? 💰 Let’s dive in!",
"Hey Blob crew! Which projects have you fired up for today?"
]

topic_list_refined = []

for topic in topic_list:
    splitted_topic = topic.replace('"', '')
    topic_list_refined.append(splitted_topic)
    
with open('config.json', 'r') as json_file:
    config = json.load(json_file)
    
# Define the file name
file_name = config['data_dir'] + "/random_message.txt"

# Write the list to the file
with open(file_name, "w") as file:
    for item in topic_list_refined:
        file.write(f"{item}\n")

print(f"List saved to {file_name}")