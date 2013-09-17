HELLO FRIEND!

You've reached my Python program for reading basic text files. The need for this is because 
I recently came across a textbook on GitHub that was written entirely in the basic text
format and needed a way to navigate it easily. Support is included for extracting hypertext
links from the text (with a menu for opening websites from the console) and also searching 
for specific terms. 

DISCLAIMER

This program was a toy designed to help me figure out how to use python dictionaries, regular expressions,
and file operations productively. If the line breaks bother you, then I would recommend you come up with ways 
to improve this program and contact me! I love constructive criticism and I'm only trying to get better at this!

SETUP

This program will require a Windows(XP/VISTA/7) in which the following are true:

- Mozilla Firefox is downloaded in the path: C:\Program Files\Mozilla Firefox\firefox.exe
- Python (ideally at least v 2.7, since that is what I made it in) is installed on the computer AND is set as a PATH in the environment variables. You can tell this is the case if you open your Command Prompt, type in "python" and get the Python
environment, no matter what directory you are in. Most Macs nowadays have Python automatically installed in their Terminals; unfortunately I am not so sure batch files work on Macs. 

The following files will need to be in the folder:
-readfile.bat : Click on this to start the program.
-readTXT.py: This is the meat of the program. The .bat file compiles this for YOU!
-README.txt: You are reading this now! I hope it is helpful.

STARTING THE PROGRAM

-To start the program, click on the file "readfile.bat". It will tell you the current directory and ask you to input the path of
the basic text file you wish to read. Conventions for writing the directory will work here (i.e. ../ will work, as does ./). To test that the program works, try to input the following path: "./README.txt"
-The next prompt will ask if you want to start at another page or not. "Y" will lead it to ask you which page. "N" will start on page one.

USING THE PROGRAM
-Pages are spit out 10 lines at a time. The length of the page is determined on the text author's formatting preferences. 
-To go to the next page, press ENTER.
-The following words can be typed + ENTER to yield the following results:
  -- "HELP": will bring up the help menu
  -- "GOTO": will bring up the page skip feature
  -- "FIND": will bring up the search term feature. 
  -- "BACK": will bring up the previous page
  -- "LINKS": will search the current page for any string starting with "http://". It will then 
  bring up a numbered list of the links. Typing in a number + ENTER will bring up the site with Firefox
  -- "EXIT": will infuriate you for a long time. Just exit out of the console.

CONTACT ME
-I can be reached at dpaolomercado@gmail.com. Let me know if there's anyway I can improve my beautiful toy.
