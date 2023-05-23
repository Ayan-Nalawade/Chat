# Chat
Access multiple models such as gpt-3/3.5, gpt-4, claude+, claude-instant for free!


**CREDITS**
Poe-API  - ading2210 (https://github.com/ading2210/poe-api)  

> For creating the program responsible to connect and "talk" with models in the website https://poe.com

FreeGPT4 - Lomusire (https://github.com/Lomusire/FreeGPT-4)

> For creating a program capable to create tokens, They also own a very cool discord server, I would recommend joining it!

***Thank you very much for your contributions!***



**Requirements and setup**

Python3 Should be installed on your system

```
git clone https://github.com/Ayan-Nalawade/Chat.git
```
**Install the repository**
```
python -m requirements.txt
```
OR
```
python3 -m requirements.txt
```

**Notes and usage**

Program by default will cycle through available and WORKING api's
Each api will be connected for 10 requests to avoid overloading singular api

use `--no-logs` if your having any issues with respond speeds or the program working at all..This command prevents context between different models/api's

*In-cli commands*

`exit` : Quite straight forward, exits the program and is the PROPER way to exit this program

`switch <model name>`: Switch between different models, at the end of each output, the program will display a list of available models, use the name on the left, for example, *gpt-4* would be *beaver*

`clear context` or `cls_context`: Remove any sort of context; from local files, and from *poe*

***If you have any further questions, or suggestions, feel free to create a thread*** 
