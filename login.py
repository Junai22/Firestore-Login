# <----- Imports -----> #

import collections
import json
import os
import sys
from typing import Collection
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# <----- Imports -----> #

# Firestore Login

cred = credentials.Certificate("./database/credentials.json") # Download Credentials at https://console.cloud.google.com/iam-admin/serviceaccounts
firebase_admin.initialize_app(cred)
db = firestore.client()

# Clear

def clear():
    os.system("cls" if "win" in sys.platform else "clear")


# Main Login

def mainlogin():
    options = input(""" 
                
    <--------------------------------->   
    |        -----------              |
    |        | Options |              |
    |        -----------              |
    |    < 1 > Login                  |
    |    < 2 > Register               |
    |                                 | 
    <--------------------------------->    
    
        Select: """)


    # Register System

    if options == "2":  
        
     clear()
     
     # Inputs
      
     username_register = input("Username: ")
     password_register = input("Password: ")
     
     clear()
     
     # Insert Data to Database
    
     principal_db = db.collection("users").document(username_register)
     principal_db.set({
            'username': username_register,
            'password': password_register
                      })
     
     clear()
     
     print("Register Succesfully.")
     mainlogin()
    
    else: 
        
        # Login System
        
        clear()
    
        # Inputs
    
        usernamelogin = input("Username: ")
        passwordlogin = input("Password: ")
        
        clear()
        
        # Get Data from Database
        
        principal_db = db.collection("users").document(usernamelogin)
        doc = principal_db.get()
        
        if doc.exists:
            
            parsejson = doc.to_dict()
            
            if passwordlogin == parsejson['password']:     
                print("Login succesfully.")

            else:
                print("Password error.")
       
        else:
            
            clear()
            
            print("Username invalid.")

mainlogin()
