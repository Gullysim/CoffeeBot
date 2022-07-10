#My coffee bot Amir Haziza version 1.2
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
surname = input("Please insert your last name --> ")
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
      print("Username taken Please choose an other one, or the mail address is all registered before.")
def code_gen():
    code = random.randint(100000, 999999)
    return code
code = code_gen()


def register(email,code):
      print(f"Sending verification mail to {email}....")
      email_to = f'{email}'
      subject = 'Hye, we are at your service, your coffee buddy'
      body = f"""
Hye there {name} {surname} In order to register to our coffee bot please insert the code {code} to the bot .
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
def Forgot_Password(email):


    for i in database.find({"Email":f"{email}"}):
        a = i["Username"]
        b = i["Password"]
        print(f"Sending Friendly Reminder to {email}....")
    email_to = f'{email}'
    subject = 'Hye, we are at your service, your coffee buddy'
    body = f"""
Hye there {a}, In case you forgot your Password ;) , we've got you covered. \nYour password is {b} 
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
def Forgot_Username(email):


    for i in database.find({"Email":f"{email}"}):
        a = i["Username"]
        b = i["Password"]
        print(f"Sending Friendly Reminder to {email}....")
    email_to = f'{email}'
    subject = 'Hye, we are at your service, your coffee buddy'
    body = f"""
Hye there your user name is {a},and In case you forgot your Password as well ;) , we've got you covered. \nYour password is {b} 
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
def Reset_Password(mail):
    new_pass = input("Insert new password --> ")
    for i in database.find({"Email":f"{mail}"}):
        my_query = {"Password": i["Password"]}
        update = {"$set": {"Password":f"{new_pass}"}}
        database.update_one(my_query,update)
        for i in database.find({"Email":f"{mail}"}):
            print(f"Sending Friendly Email with the new credentials to {mail}....")
            a = i["Username"]
            b = i["Password"]
            email_to = f'{mail}'
            subject = 'Hye, we are at your service, your coffee buddy'
            body = f"""
Hye there {a}, we updated your Password ;) , I've told told we've got you covered. \nYour new password is {b} .
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
def Delete_Account(mail):
    for i in database.find({"Email":f"{mail}"}):
        del_acc = i
        a = i["Username"]
        database.delete_one(del_acc)
        email_to = f'{mail}'
        subject = 'Hye, we are at your service, your coffee buddy'
        body = f"""
We are sorry to see you leave {a}, you always can come back to our bot:) .
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
        print("Account Successfully deleted!")
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
                fin = True
                return fin
            else:
                fin = False
      return fin        

def main():
      try:
            hello(name,surname)
            usr = input("Would you like to register to our CoffeeBot? Y\\N\n"
            "If you allready regisered please press R \n"
            "For more options Please press P -- Y\\N\\R\\P --> ")
            if usr == 'n' or usr == 'N':
                  print("Continuing as guest...")
            elif usr == 'r' or usr == 'R':
                  inp_a = input("Please insert your user name here --> ")
                  inp_b = input("Please insert your password here --> ")
                  login = Auth1(inp_a,inp_b)
                  if login == True:
                        print("Logged in successfully!! PLEASE ENJOY.")
                  elif login == False:
                        print("Logged in failed!! ACCESS DENIED.")
            elif usr == 'p' or usr == 'P':
                  more_opt = input(""
                  "[A] Forgot Password.\n"
                  "[B] Reset Password.\n"
                  "[C] Forgot username.\n"
                  "[D] Delete Account.\n"
                  "[E] Go Back.\n"
                  "INSERT YOUR CHIOCE HERE --> ")  
                  if more_opt == 'a' or more_opt == 'A':
                        email = input("It's cool, we'll send you a little reminder, just DROP YOUR EMAIL ADDRESS IN THIS SECTION --> ")
                        Forgot_Password(email)
                  elif more_opt == 'b' or more_opt == 'B':
                        email = input("It's cool, we can update your password, just DROP YOUR EMAIL ADDRESS IN THIS SECTION --> ")
                        Reset_Password(email)
                  elif more_opt == 'c' or more_opt == 'C':
                        email = input("It's cool, we'll send you a little reminder, just DROP YOUR EMAIL ADDRESS IN THIS SECTION --> ")
                        Forgot_Username(email)
                  elif more_opt == 'd' or more_opt == 'D':
                        email = input(":( If you sure you would you like to delete your account, just DROP YOUR EMAIL ADDRESS IN THIS SECTION --> ")
                        Delete_Account(email)
                  elif more_opt == 'e' or more_opt == 'E':
                        main()    
            elif usr == 'Y' or usr == 'y':
                  user_name = input("Please insert your user name here --> ")
                  password = input("Please insert your password here --> ")
                  email = input("Please insert your Email here -- > ")
                  for i in range(50):
                        for i in database.find({"Type":"Registered"}):
                              duplic_chk = (i["Username"])
                              email_chk = (i["Email"])
                              while user_name == duplic_chk or email == email_chk:
                                    duplic = True
                                    data()
                                    user_name = input("Please insert your user name here --> ")
                                    password = input("Please insert your password here --> ")
                                    email = input("Please insert your Email here -- > ")
                                    if duplic != True:
                                          break
                  register(email,code)
                  user_auth = int(input("2 Step Verification!\nPlease insert the six digits code here --> "))
                #   print(code)
                #   print(type(code))
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