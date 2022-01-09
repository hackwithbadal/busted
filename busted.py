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
def usage():
    print("usage:")
    print("     run the program         = python busted.py")
    print("     format for txt file     = /directory/.../directory/list.txt")
    print("     format for URL          = http://example.com:port/")
    print("                               Not necesary to give port number (to avoid error simple copy the URL from browser and paste.")
    print("     format for status code  = .txt ,.php,.xml,.py,.aspx,.do (Any one extention at a time)")
    print("")
usage()
path_to_file = str(input("Path to file(Press Enter For Default)->")) or 'list20k.txt'
try:
    with open(path_to_file,'r') as f:
        data = f.read()
        words = data.split()
        totalWords = len(words)
        print('totol word in file',totalWords)
except:
    print('Invalid file path !\n')
    usage()
lines = []
with open(path_to_file,'r') as f:
    lines = f.readlines()
count = 0
URL = str(input("Enter URL here(eg.https://www.youtube.com/) ->"))
extention = str(input("DO you want to cheak for specific extention(Press Enter for None :)")) or None
print(f"|=================================================|")
print(f"  text file     =  {path_to_file}")
print(f"  URL           =  {URL}")
print(f"  Status Code   =  200,403,404")
print(f"  Extention     =  {extention}")
print(f"|=================================================|")
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
        print("Connection to Website Fail\nPlease Copy URL from Browser and paste again ",e,'\n')
        usage()
        break