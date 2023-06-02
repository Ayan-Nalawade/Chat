# Chat
Access multiple models such as gpt-3/3.5, gpt-4, claude+, claude-instant for free!

***Currently the program is facing some errors, we are working on resolving them ASAP!***

***Replit Example is currently not working, once I get a reliable way of hosting the `bard_token`, it will be up again, I apologize for this***

**CREDITS**
Poe-API  - ading2210 (https://github.com/ading2210/poe-api)  

> For creating the program responsible to connect and "talk" with models in the website https://poe.com

FreeGPT4 - Lomusire (https://github.com/Lomusire/FreeGPT-4)

> For creating a program capable to create tokens, They also own a very cool discord server, I would recommend joining it!

Bard-API - dsdanielpark (https://github.com/dsdanielpark/Bard-API)

> For creating a program capable to connect and get responce from Bard.


## Requirements and setup

Python3 Should be installed on your system

```
git clone https://github.com/Ayan-Nalawade/Chat.git
```
**Install the repository**
```
pip install -r requirements.txt
```

### Setup Bard API

1. Go to [bard.google.com](https://bard.google.com/)

2. Sign in with a google/bard approved account (***Required to use google bard api***)

3. Press `F12` or `ctrl + shift + i` for google dev or console

4. Session: Application → Cookies → Copy the value of `__Secure-1PSID` cookie.

5. Open chatv1.1.py using any text editor, and replace `'CHANGE ME!'` in variable `bard_token` to value aquired on point 4 

***Click [Here](https://github.com/dsdanielpark/Bard-API) for more info***

### Setup discord api

***NOTE: Having it open on the website is required here and have the developer mode on, read below on how to turn it on!!***

1. Join the discord server: https://discord.gg/v5mqTMjmFn

3. Press `ctrl + shift + i` to open chrome dev -> Then navigate to the 'network' tab
![image](https://github.com/Ayan-Nalawade/Chat/assets/108238535/70cfdb6b-b052-4f21-a9bb-e8a0384bf433)

3. GRAB authentication: Go to any of the '-ai-chatroom', then type something, like `!info`
![image](https://github.com/Ayan-Nalawade/Chat/assets/108238535/441e3306-fa8b-42b3-9dde-dda0566585b5)

4. GRAB channel ID: Go to `poe-token` and copy the channel id

![image](https://github.com/Ayan-Nalawade/Chat/assets/108238535/71fee924-d88b-4921-b734-8be15aac9df5)

5. Put information from STEP 3 into the `auth` variable in the chatv1.py
6. Put information from STEP 4 into the `id` variable in the chatv1.py

![image](https://github.com/Ayan-Nalawade/Chat/assets/108238535/5743ee5d-97f1-4f64-99a0-a91a36fd0e3b)

**How to turn developer mode on in discord**

1. Click on the settings on the user profile
![image](https://github.com/Ayan-Nalawade/Chat/assets/108238535/974a3245-da57-449e-838a-e16c9a69cb17)
2. Click on the advanced tab and then turn on developer mode
![image](https://github.com/Ayan-Nalawade/Chat/assets/108238535/bbf6c731-b6af-4faa-b5bd-d48cc5a7f3bc)



## Notes and usage

Program by default will cycle through available and WORKING api's
Each api will be connected for certain amount of requests to avoid overloading singular api

*In-cli commands*

`!exit` : Quite straight forward, exits the program and is the PROPER way to exit this program

`<model_name> : <text>`: Use this to talk to a model, if unsure, type `help : help` to get bot names

`!index`: Remove current *working* api's and re-grab the working api's, this may take a bit depending on your CPU, RAM and network speed

**Currently Working on...**
1. Adding Bing AI

***If you have any further questions, or suggestions, feel free to create a thread*** 
