
# @elbee_ez

####################################################################################
# Alien Camp | Difficulty: 1-star | Misc ###########################################
####################################################################################
# The Ministry of Galactic Defense now #############################################
# accepts human applicants for their specialised ###################################
# warrior unit, in exchange for their debt to be ###################################
# erased. We do not want to subject our people to ##################################
# this training and to be used as pawns in their ###################################
# little games. We need you to answer 500 of their #################################
# questions to pass their test and take them #######################################
# down from the inside. This challenge will ########################################
# raise 33 euros for a good cause. #################################################
####################################################################################



from pwn import *
import re

rhost='138.68.185.219'
rport=31903

dict = {}

s = remote(rhost,rport)
s.recvuntil(b'test!')
s.sendline(b'1')
s.recvline()
s.recvline()
s.recvline()
emoji_help = s.recvline()
emoji_help = emoji_help.decode("utf-8")
count = 0
string = ""

for char in emoji_help:
    string += char
    if char == " ":
        count += 1
        if count == 3:
            string += "\n"
            count = 0

string = string.replace(" -> ", ": ")
string = string.replace("\n", ", ")
string = string.replace(" , ", ", ")
string = ', '+string

emojis = string.split(', ')

for a in range(0,len(emojis)):
	emojis[a] = emojis[a].split(': ')

emojis = emojis[1:-2]
for c in range(0,len(emojis)):
	dict[emojis[c][0]] = emojis[c][1]

### send shit

print("="*120)
print("Key is..")
print(dict)
print("="*120)

s.sendline(b'2')

for o in range(1,9):
	s.recvline()

for i in range(1,502):
	equation=str(s.recvline())
	equation=equation[2:-8]
	if i==502:
		print(str(s.recvuntil(b"}")))
	print("#"*120)
	print("Ques. "+str(i))
	print("Before translation: "+equation)
	print("#"*120)
	if "\\xF0\\x9F\\x8C\\x9E".lower() in equation:
		equation = equation.replace("\\xf0\\x9f\\x8c\\x9e".lower(), dict.get('🌞'))
	if "\\xF0\\x9F\\x8D\\xA8".lower() in equation:
		equation = equation.replace("\\xF0\\x9F\\x8D\\xA8".lower(), dict.get('🍨'))
	if "\\xE2\\x9D\\x8C".lower() in equation:
		equation = equation.replace("\\xE2\\x9D\\x8C".lower(), dict.get('❌'))
	if "\\xF0\\x9F\\x8D\\xAA".lower() in equation:
		equation = equation.replace("\\xF0\\x9F\\x8D\\xAA".lower(), dict.get('🍪'))
	if "\\xF0\\x9F\\x94\\xA5".lower() in equation:
		equation = equation.replace("\\xF0\\x9F\\x94\\xA5".lower(), dict.get('🔥'))
	if "\\xE2\\x9B\\x94".lower() in equation:
		equation = equation.replace("\\xE2\\x9B\\x94".lower(), dict.get('⛔'))
	if "\\xF0\\x9F\\x8D\\xA7".lower() in equation:
		equation = equation.replace("\\xF0\\x9F\\x8D\\xA7".lower(), dict.get('🍧'))
	if "\\xF0\\x9F\\x91\\xBA".lower() in equation:
		equation = equation.replace("\\xF0\\x9F\\x91\\xBA".lower(), dict.get('👺'))
	if "\\xF0\\x9F\\x91\\xBE".lower() in equation:
		equation = equation.replace("\\xF0\\x9F\\x91\\xBE".lower(), dict.get('👾'))
	if "\\xF0\\x9F\\xA6\\x84".lower() in equation:
		equation = equation.replace("\\xF0\\x9F\\xA6\\x84".lower(), dict.get('🦄'))
	answer = str(eval(equation))
	print("After translation: "+equation+" = "+answer)
	print("#"*120)
	s.sendline(answer)
	s.recvline()
	s.recvline()
	s.recvline()
	s.recvline()
	s.recvline()
	s.recvline()
	print("\n\n")
