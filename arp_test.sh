#! /bin/bash

i=1

while [ "$i" != "101" ]
do
	sudo ./scp_arp.py
	i=$(($i+1))
done
