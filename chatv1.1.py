from bardapi import Bard
import poe
from hashlib import sha1
from colorama import Fore, Back
import gzip, os, platform, sys, colorama, ctypes, struct, json, requests, time, logging, concurrent.futures, random

colorama.init(autoreset=True)
logging.getLogger('poe-api').setLevel(logging.CRITICAL)

tokens = []
auth = "CHANGE ME!"
id = "CHANGE ME!"
bard_token = 'CHANGE ME!'


def print_banner():
    if platform.system() == "Windows":
      kernel32 = ctypes.windll.kernel32
      handle = kernel32.GetStdHandle(-11)
      csbi = ctypes.create_string_buffer(22)
      res = kernel32.GetConsoleScreenBufferInfo(handle, csbi)
  
      if res:
          _, _, _, _, _, left, top, right, bottom, _, _ = struct.unpack("hhhhHhhhhhh", csbi.raw)
          width = right - left + 1
          height = bottom - top + 1
      else:
          width = os.terminal_size(80)
          height = os.terminal_size(24)
      
      if os.name == 'nt':
          terminal_size = os.terminal_size((width, height))
          width = terminal_size.columns
  
          print(Fore.GREEN +'*' * width)
          print(Fore.GREEN + f'* {"Product Name: Chat".center(width - 4)} *')
          print(Fore.GREEN + f'* {"Author: Ayan Nalawade".center(width - 4)} *')
          print(Fore.GREEN + '*' * width)
    else:
      print(Fore.GREEN +'*' * 80)
      print(Fore.GREEN + f'* {"Product Name: Chat".center(80 - 4)} *')
      print(Fore.GREEN + f'* {"Author: Ayan Nalawade".center(80 - 4)} *')
      print(Fore.GREEN + '*' * 80)

def retrieve_messages(channel_id: int, limit:int = 100) -> None:
    try:
        headers = {
            'authorization': auth
        }
        url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
        params = {'limit': limit} 
        tmp_count = 0
        while True:
            r = requests.get(url, headers=headers, params=params)
            jsonn = json.loads(r.text)
            for value in jsonn:
                tokens.append(value['content'])
                print(f"\r Found {tmp_count} Tokens", end='')
                tmp_count += 1
            if len(jsonn) < limit:
                break
            else:
                last_message_id = jsonn[-1]['id']
                params['before'] = last_message_id
    except Exception:
        print(f"{Fore.RED} Error: Make sure your internet connection is on and supports discord, you can verify by going to discord.com")
        sys.exit(0)
    
print_banner()   

def check_token(index, each):
    headers = {"Cookie": f"p-b={each}"}
    url = "https://poe.com/settings"
    
    try:
        with requests.get(url, headers=headers) as response:
            cntnt = response.text
            if 'manage subscription' in cntnt.lower():
                return (index, each)
    except Exception:
        pass
    return (index, None)

def print_progress(progress, total, active_count, start_time):
    elapsed_time = time.time() - start_time
    estimated_remaining = int(((elapsed_time / (progress+1)) * (total - (progress+1))))
    print(f"\r Stats: {progress+1}/{total} tokens, {active_count} active, estimated remaining: {estimated_remaining} second(s)               ", end='')

def main(tokens):
    active = []
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(check_token, index, each): (index, each) for index, each in enumerate(tokens)}

        for future in concurrent.futures.as_completed(futures):
            index, result = future.result()
            if result is not None:
                active.append(result)
            print_progress(index, len(tokens), len(active), start_time)

    return active

def pr_botnames(local_client) -> None:
  count = 1
  for key, value in local_client.bot_names.items():
    print(f"{Fore.CYAN} {value}")
    count += 1

def name_exchange(client_instance, model_name):
    for key, value in client_instance.bot_names.items():
        if value.lower() == model_name.lower():
            return key
    return None

def index():
  if not os.path.exists("./index.gz"):
    print(f"\r {Fore.RED} This program needs to index tokens before they can be used, please press ENTER to continue", end='')
    input()
    retrieve_messages(id)
    # Run the main function
    active = main(tokens)
    
    with gzip.open("index.gz", mode='wt') as ptr:
      for each in active:
        ptr.write(each)

    print(f"{Fore.YELLOW} \n Complete! Please relaunch program and start chatting! Press ENTER to exit for now")
    input()
    sys.exit(0)
  else:
    active = ""
    with gzip.open("index.gz", mode="rt") as ptr:
      for line in ptr:
          active += str(line.split("%3D%3D"))
    #print(active)
  
  
  
  tmp = ""
  active_tok = []
  for each in active:
    if each.isalnum():
      tmp += each
    elif each == "'":
      active_tok.append(f"{tmp}%3D%3D")
      tmp = ""
  for each in active_tok:
    if each == "%3D%3D":
      active_tok.remove(each)

  return active_tok

active_tok = index()

ccount = random.randint(0, len(active_tok))
while True:
  if ccount >= len(active_tok):
      ccount = 0
  print("\n")
  iter_inp = input(f"{sha1(active_tok[ccount].encode()).hexdigest()} > ")
  if "!index" in iter_inp.lower():
    if os.path.exists("./index.gz"):
      os.remove("./index.gz")
    index()
  elif "!exit" in iter_inp.lower():
    sys.exit(0)
      
  try:
    bot, text = iter_inp.split(":")
    # text = text.replace(" ", "")
    bot = bot.replace(" ", "")
  except:
    print(f"{Fore.LIGHTYELLOW_EX} Invalid Syntax, please respond with <Model Name> : <text input>, ex: GPT-4 : write a haiku on peaceful sitting in a forest")
    continue

  if bot.lower() == "bard":
    try:
      bard = Bard(token=bard_token)
      print(Fore.WHITE + Back.BLACK + bard.get_answer(text)['content'])
      continue
    except Exception:
      print("\r We ran into some difficulty...", end='')
      continue
    
  
  try:
    client = poe.Client(active_tok[ccount])
    bot = name_exchange(client, bot)
    if bot == None:
      print(f"{Fore.LIGHTYELLOW_EX} Invalid Bot name, use one of the following: \n")
      pr_botnames(client)
      print(f"{Fore.CYAN} Bard")
      continue
    client.purge_conversation(bot)
    for chunk in client.send_message(bot, text):
      print(Fore.WHITE + Back.BLACK + chunk["text_new"], end="",flush=True)
  except Exception as s:
    print("\r We ran into some difficulty...", end='')
    continue
  finally:
    ccount += 1
  