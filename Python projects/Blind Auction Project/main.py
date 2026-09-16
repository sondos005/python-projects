# TODO-1: Ask the user for input
import art
print(art.logo)

def user(name,price):
    data1[name]=price
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
list1=[]
data1 ={}
winner = ""
cont=True
while cont == True:
    name=input("what is your name?")
    price=int(input("what is your bid?"))
    user(name,price)
    valueOfCont=input("do you want to continue? yes or no").lower()
    if valueOfCont== "no":
        cont=False
        for x in data1:
            list1.append(data1[x])
        res= max(list1)
        for x in data1:
            if data1[x] == res:
                 winner = x
        print(f"the winner is {winner} ")
    else:
        print("\n" * 20)