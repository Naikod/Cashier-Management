import time
from os import system, name
DataSales = {}
def modifyData(mode, itemID, itemPrice):
	if mode == 1:
		DataSales.update({itemID: itemPrice})
	elif mode == 2:
		del DataSales[itemID]
	else:
		DataSales.update({itemID: itemPrice})
	print("Success!")
	time.sleep(2)
	Page()

def error():
	print("Error handler: unknown error issue")
	time.sleep(2)
	return Page()

def Page():
	system("cls")
	print("[1] Transaction\n[2] Modify item\n")
	modeinput = int(input(":"))
	if modeinput > 2:
		error()
		time.sleep(2)
	elif modeinput == 1:
		cashier = True
		print("Write `91000100` to exit the cashier section")
		total = 0
		while cashier == True:
			itemID = int(input("ItemID: "))
			if itemID in DataSales:
				total = total + DataSales[itemID]
			elif itemID == 91000100:
				cashier == False
				print("Total: ",total)
				time.sleep(5)
				error()
			else:
				print("We can't find this item id!")
				time.sleep(2)
			
	else:
		DataType = int(input("[1] Add Item\n[2] Remove Item\n[3] Change item price data"))
		if DataType == 1:
			print("Please input:")
			itemID = int(input("ItemID: "))
			if itemID in DataSales:
				itemPrice = int(input("Price: "))
				modifyData(1, itemID, itemPrice)
			else:
				error()
		elif DataType == 2:
			print("Please input:")
			itemID = int(input("ItemID: "))
			if itemID in DataSales:
				modifyData(2, itemID, 0)
			else:
				error()
		elif DataType == 3:
			print("Please input:")
			itemID = int(input("ItemID: "))
			if itemID in DataSales:
				print("Default price of ",itemID,"is",DataSales.get(itemID))
				newItemPrice = int(input("New Item Price: "))
				modifyData(3, itemID, newItemPrice)
			else:
				error()
		else:
			error()
Page()
