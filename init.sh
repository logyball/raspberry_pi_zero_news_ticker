#!/bin/bash

sudo apt-get update
sudo apt-get install python3-pip python3-scrollphathd -y

sudo $(which pip3) install -r requirements.txt
sudo $(which python3) polling.py
