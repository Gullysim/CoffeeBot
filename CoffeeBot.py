#My coffee bot Amir Haziza version 1.0#
import pymongo
import time
import ssl
from email.message import EmailMessage
import smtplib
import random
import os
from dotenv import load_dotenv
load_dotenv()
db_creds = os.getenv("db_creds")
env1 = os.getenv("env1")
env2 = os.getenv("env2")
print("Hello and welcome to our Coffee Bot version 1.0 Developed by Amir Haziza.\n\n"
      "Your Coffee orders will sent from our bot to our working department kitchen directly.\n")
client = pymongo.MongoClient(f"mongodb+srv://{db_creds}.l2zbb.mongodb.net/?retryWrites=true&w=majority")
db = client.test
CoffeeBotDB = client["CoffeeBotDB"]
database = CoffeeBotDB["userDB"]
email_from = f"{env1}"
email_pass = f"{env2}"
name = input("Please insert your first name --> ")
surname = input("Pleases insert your last name --> ")
def hello(name,surname):
      name = name.capitalize()
      surname = surname.capitalize()
      user_choice = input(f"Hye there {name} {surname} press any key to continue, to exit the bot press q.")
      if user_choice == 'q' or user_choice == 'Q':
            print(f"See you next time, have a great day {name}!")
            exit()
      else:
            pass
      name_data = {"First Name":f"{name}","Surname":f"{surname}"}
      return name_data

def data():
      print("Username taken Please choose an other one.")
def code_gen():
    code = random.randint(100000, 999999)
    return code
code = code_gen()


def register(email,code):
      print(f"Sending verification mail to {email}....")
      email_to = f'{email}'
      subject = 'Hye, we are at your service, your coffee buddy'
      body = f"""
            In order to register  to our coffee bot please insert the code {code} to the bot .
            """
      em = EmailMessage()
      em['From'] = email_from
      em['To'] = email_to
      em['Subject'] = subject
      em.set_content(body)
      context = ssl.create_default_context()
      with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_from, email_pass)
            smtp.sendmail(email_from, email_to, em.as_string())
def sign_up(email,user_name,password):
      data = {"Type": "Registered", "Email": f"{email}", "Username": f'{user_name}', "Password": f'{password}'}
      database.insert_one(data)

def Auth1(inp_a,inp_b):


    for i in database.find({"Type":"Registered"}):
        a = i["Username"]
        b = i["Password"]
        db = {f'{a}',f'{b}'}
        for key in db:
            if inp_a == a and inp_b == b:
                lo  = True
                return lo
            else:
                lo = False
    return lo  
def main():
      try:
            hello(name,surname)
            usr = input("Would you like to register to our CoffeeBot? Y\\N\n"
            "If you allready registred please press --> \R INSERT HERE ")
            if usr == 'n' or usr == 'N':
                  print("Continuing as guest...")
            elif usr == 'r' or usr == 'R':
                  inp_a = input("-->")
                  inp_b = input("-->")
                  login = Auth1(inp_a,inp_b)
                  if login == True:
                        print("Logged in successfully!! PLEASE ENJOY.")
                  elif login == False:
                        print("Logged in failed!! ACCESS DENIED.")

            elif usr == 'Y' or usr == 'y':
                  user_name = input("Please insert your user name here --> ")
                  password = input("Please insert your password here --> ")
                  email = input("Please insert your Email here -- > ")
                  for i in range(100):
                        for i in database.find({"Type":"Registered"}):
                              duplic_chk = (i["Username"])
                              while user_name == duplic_chk:
                                    duplic = True
                                    data()
                                    user_name = input("Please insert your user name here --> ")
                                    password = input("Please insert your password here --> ")
                                    email = input("Please insert your Email here -- > ")
                                    if duplic != True:
                                          break
                  register(email,code)
                  user_auth = int(input("2 Step Verification!\nPlease insert the six digits code here --> "))
                  print(code)
                  print(type(code))
                  if user_auth == code:
                        print("Signed up successfully!!")
                        sign_up(email,user_name,password)
                  else:
                        print("Something went wrong with the code inserted, please try again.")
      except Exception as e:
            print(e)
      finish = input("Press any key to launch the bot once again, reply 'q' to exit the bot. --> ")
      if finish == 'q' or finish == 'Q':
            exit()
      else:
            main()
main()











code_gen()




















# def duplication(user_name):
#       for x in database.find({"Type" : "Registered"},{"_id":0,"Username":1}):
#             usr_name_val = (x["Username"])
#             if user_name == usr_name_val:
#                   return False
#             else:
#                   return True
# def greet(name):
#       sign_in = input(f"Hye {name}, would you like to register to our CoffeeBot. Y\\N --> ")
#       if sign_in == 'Y' or sign_in == 'y':
#             print("We are glad that you choose to register to our bot!\n")
#             user_name = input("Please enter user name --> ")
#             password = input("Please enter your password --> ")
#             print(duplication(user_name))
#             data = {"Type" : "Registered","Username" : f'{user_name}', "Password" : f'{password}'}
#             dup = duplication(user_name)
#             print(dup)
#             while dup is False:
#                   print("Username Taken! Please choose an other one.")
#                   greet(name)
#             else:
#                   database.insert_one(data)
#       else:
#             pass
# greet(name)
