#!/bin/bash

apt-get update
apt install python3-pip -y

$(which pip3) install -r requirements.txt
$(which python3) polling.py
