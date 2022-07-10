# import pymongo
# client = pymongo.MongoClient(f"mongodb+srv://yaniv:Dvg2246mx1@coffeebot.l2zbb.mongodb.net/?retryWrites=true&w=majority")
# db = client.test 
# CoffeeBotDB = client["CoffeeBotDB"]
# database = CoffeeBotDB["userDB"]
# inp_a = input("---->")
# inp_b = input("----->")


# def Auth1(inp_a,inp_b):


#     for i in database.find({"Type":"Registered"}):
#         a = i["Username"]
#         b = i["Password"]
#         db = {f'{a}',f'{b}'}
#         for key in db:
#             if inp_a == a and inp_b == b:
#                 lo  = True
#                 return lo
#             else:
#                 lo = False
#     return lo               

# print(Auth1(inp_a,inp_b))


# from tkinter import *
# from tkinter.ttk import *
# from time import strftime
# root = Tk()
# root.title("Clock")
# def time():
#     string = strftime('%H:%M:%S $p')
#     label.config(text=string)
# label = Label(root, font=("ds-digital", 80), background= "Red", foreground="cyan")
# label.pack(anchor='center')
# mainloop()  

# import time

# def countdown(t):
#     while t:
#         mins, secs = divmod(t,60)


# import time

# t = int(input("Seconds -->>"))
# while t:
#     mins = t//60
#     secs = t%60
#     timer = '{:02d}:{:02d}'.format(mins,secs)
#     print("Enjoy and u can play a game after the timer its done",timer, end="\r")
#     time.sleep(1)
#     t -= 1 
    
# print('Fire in the HOLE!')    
import pymongo
import time
import ssl
from email.message import EmailMessage
import smtplib
import random
import os
import Clock
from dotenv import load_dotenv
load_dotenv()
db_creds = os.getenv("db_creds")
env1 = os.getenv("env1")
env2 = os.getenv("env2")
client = pymongo.MongoClient(f"mongodb+srv://{db_creds}.l2zbb.mongodb.net/?retryWrites=true&w=majority")
db = client.test
CoffeeBotDB = client["CoffeeBotDB"]
database = CoffeeBotDB["userDB"]
# mail = input("mail:")


for i in database.find({"Type":"Registered"}):
    print(i)