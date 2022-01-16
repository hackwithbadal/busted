# badal gaidhane(IN)
# badalgaidhane16@gmail.com

from functools import update_wrapper
import sys
from typing import Mapping
import requests
import time
bar = [
    " [=>                                         ]",
    " [  =>                                       ]",
    " [    =>                                     ]",
    " [      =>                                   ]",
    " [        =>                                 ]",
    " [          =>                               ]",
    " [            =>                             ]",
    " [              =>                           ]",
    " [                =>                         ]",
    " [                  =>                       ]",
    " [                    =>                     ]",
    " [                      =>                   ]",
    " [                        =>                 ]",
    " [                          =>               ]",
    " [                            =>             ]",
    " [                              =>           ]",
    " [                                =>         ]",
    " [                                  =>       ]",
    " [                                    =>     ]",
    " [                                      =>   ]",
    " [                                        => ]",
    " [                                         =>]",
]
def intro():
    print(" ____   ____       ____    _    ____    _    _")  
    print("| __ ) / ___|     | __ )  / \  |  _ \  / \  | |") 
    print("|  _ \| |  _      |  _ \ / _ \ | | | |/ _ \ | |")    
    print("| |_) | |_| |     | |_) / ___ \| |_| / ___ \| |___")
    print("|____/ \____|     |____/_/   \_\____/_/   \_\_____|")
    print("\t\t\t©corpright badal gaidhane 2022\n")
intro()
def usage():
    print("Usage:")
    print("     run the program  = python busted.py -u http://www.example.com/ -w /path1/path2/list.txt")
    print("     -u(URL)          = http://example.com:port/ not necesary to give port number (to avoid error simple copy the URL from browser and paste")
    print("     -w(WORDLIST)     = /directory/.../directory/list.txt")

n = len(sys.argv)

# python3 busted.py -u URL -w WORDLIST -e EXTENTION
#               0    1  2   3     4     5     6

if n <= 4:
    print("Insufficient arguments ! use proper command")
    usage()
    exit()
URL = sys.argv[2]
path_to_file = sys.argv[4]


# test connection with website
response = requests.head(URL)    
if response.status_code == 200:
    pass
else:
    print("WEBSITE NOT FOUND")
    usage()
    exit()

# checking and opening the wordlist
try:
    with open(path_to_file,'r') as f:
        data = f.read()
        words = data.split()
        totalWords = len(words)
except:
    print('Invalid wordlist path !')
    usage()
    exit()

# extentions



lines = []
with open(path_to_file,'r') as f:
    lines = f.readlines()
print(f"|=================================================|")
print(f" Running script   = {sys.argv[0]}")
print(f" URL              = {URL}(active)")
print(f" text file        = {path_to_file}")
print(f" Word in wordlist = {totalWords}")
print(f" Status Code      = 200,403,404")
print(f"|=================================================|")

      
count = 0
for line in lines:
    # print(bar[count % len(bar)], end="\r")
    count += 1
    Update_URL = URL + line
    print("Trying ->",Update_URL)
    try:
        response = requests.head(Update_URL)    
        if response.status_code == 200:
            print('Found ! | status code = 200 | url=',Update_URL)
        elif response.status_code == 403:
            print('Found but Hidden ! | status code = 403 | url=',Update_URL)
        else:
            # print("404 Not Found !")
            pass
    except requests.ConnectionError as e:
        print("Connection to Website Fail\nPlease Copy URL from Browser and paste again ",e,'\n')
else:
    print('Process completed !')