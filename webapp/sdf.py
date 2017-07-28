insert = int(input("money"))
fee = int(input("fee"))
change = insert-fee
coin500 = change//500
coin100 = (change%500)//100
print("coin 500 : ",coin500," and coin 100 : ",coin100)
