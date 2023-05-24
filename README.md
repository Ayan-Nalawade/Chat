# Chat
Access multiple models such as gpt-3/3.5, gpt-4, claude+, claude-instant for free!

***Run this program on repl.it***
https://replit.com/@NA4543/Chat?v=1

**CREDITS**
Poe-API  - ading2210 (https://github.com/ading2210/poe-api)  

> For creating the program responsible to connect and "talk" with models in the website https://poe.com

FreeGPT4 - Lomusire (https://github.com/Lomusire/FreeGPT-4)

> For creating a program capable to create tokens, They also own a very cool discord server, I would recommend joining it!


**Requirements and setup**

Python3 Should be installed on your system

```
git clone https://github.com/Ayan-Nalawade/Chat.git
```
**Install the repository**
```
pip install -r requirements.txt
```

**Setup discord api**

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



**Notes and usage**

Program by default will cycle through available and WORKING api's
Each api will be connected for 10 requests to avoid overloading singular api

use `--no-logs` if your having any issues with respond speeds or the program working at all..This command prevents context between different models/api's

*In-cli commands*

`exit` : Quite straight forward, exits the program and is the PROPER way to exit this program

`switch <model name>`: Switch between different models, at the end of each output, the program will display a list of available models, use the name on the left, for example, *gpt-4* would be *beaver*

`clear context` or `cls_context`: Remove any sort of context; from local files, and from *poe*



***If you have any further questions, or suggestions, feel free to create a thread*** 
