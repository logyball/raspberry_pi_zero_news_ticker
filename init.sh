#!/bin/bash

apt-get update
apt-get install python3-pip python3-scrollphathd -y

$(which pip3) install -r requirements.txt
$(which python3) polling.py
