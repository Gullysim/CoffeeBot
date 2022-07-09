import pymongo
client = pymongo.MongoClient(f"mongodb+srv://yaniv:Dvg2246mx1@coffeebot.l2zbb.mongodb.net/?retryWrites=true&w=majority")
db = client.test 
CoffeeBotDB = client["CoffeeBotDB"]
database = CoffeeBotDB["userDB"]
inp_a = input("---->")
inp_b = input("----->")


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

print(Auth1(inp_a,inp_b))       


 
