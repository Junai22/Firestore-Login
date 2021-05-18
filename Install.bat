@echo off

cls

ECHO Installing the required packages!
TIMEOUT 3

py -3 -m pip install -U -r requirements.txt

ECHO Done!
py -3 login.py
