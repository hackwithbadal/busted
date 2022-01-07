from functools import update_wrapper
from typing import Mapping
import requests
def intro():
    print(" ____   ____       ____    _    ____    _    _")  
    print("| __ ) / ___|     | __ )  / \  |  _ \  / \  | |") 
    print("|  _ \| |  _      |  _ \ / _ \ | | | |/ _ \ | |")    
    print("| |_) | |_| |     | |_) / ___ \| |_| / ___ \| |___")
    print("|____/ \____|     |____/_/   \_\____/_/   \_\_____|")
    print("\t  ©corpright reserve badal gaidhane 20222")
intro()
# ----to check the number of words in file---------#
# def_path_to_file = list22k.txt
# def Url_Check():
path_to_file = str(input("Path to file(Press Enter For Default)->")) or 'list20k.txt'
try:
    with open(path_to_file,'r') as f:
        data = f.read()
        words = data.split()
        totalWords = len(words)
        print('totol word in file',totalWords)
except ValueError:
    print('Invalid file path ',ValueError)
lines = []
with open(path_to_file,'r') as f:
    lines = f.readlines()
count = 0
URL = str(input("Enter URL here(https://www.youtube.com/) ->"))
print(f"|====================================|")
print(f"  file   =  {path_to_file}")
print(f"  URL    =  {URL}")
print(f"  Status Code = 200,403,404")
print(f"|====================================|")
for line in lines:
    count += 1
    Update_URL = URL + line
    print("Trying URL ->",Update_URL)
    try:
        response = requests.head(Update_URL)    
        if response.status_code == 200:
            print('Found ! | status code = 200 | url=',Update_URL)
        elif response.status_code == 403:
            print('Found but Hidden ! | status code = 403 | url=',Update_URL)
        else:
            print("404 Not Found !")
    except requests.ConnectionError as e:
        print('Connection to Website Fail\nPlease Copy URL from Browser and paste',e)
        break