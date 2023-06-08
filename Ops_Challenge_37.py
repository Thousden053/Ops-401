#!/usr/bin/python3

#Tyler Housden

#utilized chatgpt

#!/usr/bin/env python3

import requests
import webbrowser

targetsite = "http://www.whatarecookies.com/cookietest.asp"
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster():
    print('''
              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.
        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Send the cookie back to the site and receive a HTTP response
response = requests.get(targetsite, cookies=cookie)

# Generate a .html file to capture the contents of the HTTP response
with open("response.html", "w") as file:
    file.write(response.text)

# Open the .html file with Firefox
webbrowser.get("firefox").open("response.html")

# Stretch Goal: Give Cookie Monster hands
def give_cookie_monster_hands():
    print('''
              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.
        ||          |||||
      ---------------|||----
        ||          |||||
        ''')

give_cookie_monster_hands()
