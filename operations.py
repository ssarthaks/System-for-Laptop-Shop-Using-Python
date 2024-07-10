from read import mydict,laptopview
from write import modifieddict_to_txtfile,user_order_bill,restock_laptop_bill,newstock_laptop_bill

#asking user for ID and passing to every function
def id_validation(dictt):
    while True:
        try:
            id = int(input("Enter the ID of the laptop: "))
            if id < 0 or id > len(dictt):
                print("---Please enter a Valid ID of a laptop and try again!---")
                print("\n")
            else:
                return id
        except ValueError:
            print("---Invalid input. Please enter a valid integer.---")
            print("\n")

#asking user for qnty and passing to every other function
def qnt_validation(dictt, id):
    stockqnt = int(dictt[id][3])
    while True:
        try:
            qnt = int(input("Enter the Quantity: "))
            if qnt > stockqnt or qnt < 0:
                print("---Please enter a valid Quantity!---")
                print("\n")
            else:
                return qnt
        except ValueError:
            print("---Invalid input. Please enter a valid integer.---")
            print("\n")

#asking user for shipping cost and passing to every other function
def shipcostforuser():
    #asking user if he wants to ship or not
    print("\n")
    while True:
        try:
            ship = input("Do you want laptop to be shipped to your place? (y/n) : ")
            if ship.lower() not in ["y", "n"]:
                raise ValueError("---Invalid input. Please enter 'Y' or 'N'.---")
            break  # break out of the loop if input is valid
        except ValueError as e:
            print(e)
            print("\n")

    shipcost=0
    if ship.lower() == "y":
        try:
            add = input("Do you live inside Kathmandu Valley? (Y/N): ")
            while add.lower() != "y" and add.lower() != "n":
                print("---Invalid input. Please enter 'Y' or 'N'.---")
                print("/n")
                add = input("Do you live inside Kathmandu Valley? (Y/N): ")

            if add.lower() == 'y':
                shipcost = 500
            elif add.lower() == 'n':
                shipcost = 1000

        except ValueError as e:
            print(e)
            print("\n")
    return shipcost

#asking user for details of buyer and passing to every other function
def details_for_bill():
    print("\n")
    name = input("Enter your name : ")
    address = input("Enter your address : ")
    phone = input("Enter your phone number : ")
    return name,address,phone

#main function for user order
#this function purchases the laptop and displays the bill to textfile n console
def orderlaptop():
    #creating an empty 2d list
    user_laptops=[]
    #storing the dictionary data from mydict() function to a new variable
    dictt=mydict()
    print("\n")
    print("\t\t\t\t\t\t\t💻 𝑶𝒓𝒅𝒆𝒓 𝑺𝒆𝒄𝒕𝒊𝒐𝒏 𝑭𝒐𝒓 𝑪𝒖𝒔𝒕𝒐𝒎𝒆𝒓 💻")
    #calling function
    laptopview()
    #calling function
    user_ordering_laptop(dictt,user_laptops)
    '''
    here what i have basically done is getting value that has been returned from different functions and storing it in a variable 
    then i have passed those variables in bill generator function 
    '''
    shipcost = shipcostforuser()
    name,address,phone = details_for_bill()

    # Call the bill generator function to generate the bill
    user_order_bill(dictt,user_laptops,shipcost,name,address,phone)

#function for asking user id n qnt and deducting from file
def user_ordering_laptop(dictt,user_laptops):
    ch = "y"
    #loop for asking user to buy a laptop and ask him again if he wants to buy more or not
    while ch.lower() == "y":
        #value for asking id to user and storing it in id variable
        id = id_validation(dictt)
        #Checking if the given id is valid
        qnt = qnt_validation(dictt,id)
        print("\n")       
        #storing user laptop details to the 2D list created before
        nameoflaptop = dictt[id][0]
        brandoflaptop = dictt[id][1]
        priceoflaptop = dictt[id][2]
        quantityoflaptop = qnt
        processoroflaptop = dictt[id][4]
        graphicsoflaptop = dictt[id][5]
        ramoflaptop = dictt[id][6]
        memoryoflaptop = dictt[id][7]
        totalprice = int(priceoflaptop)*qnt  
        user_laptops.append([nameoflaptop, brandoflaptop, priceoflaptop, quantityoflaptop, processoroflaptop, graphicsoflaptop, ramoflaptop, memoryoflaptop, totalprice])

        #updating the record to the textfile 
        #these lines of code deducts the quantity that user bought from the total number of available quantity
        dictt[id][3] = str(int(dictt[id][3]) - qnt)

        modifieddict_to_txtfile(dictt)

        #checking if he wants to purchase other laptops or not
        while True:
            try:
                ch = input("Would you like to order another laptop ? (Y/N) : ")
                if ch.lower() not in ['y', 'n']:
                    raise ValueError("---Invalid input. Please enter 'Y' or 'N'.---")
                    print("\n")
                break  # break out of the loop if input is valid
            except ValueError as e:
                print(e)
                print("\n")

#this function is for store to buy a new laptop or restock 
def updatestorelaptops():
    #storing the dictionary data from mydict() into a new variable
    order_laptops=[]
    totallaptops=[]
    dictt = mydict()
    print("\n")
    #asking user to restock or add new laptop
    while True:
        try:
            check = input("Do you want to restock or order a new laptop? (Re / New): ")
            if check.lower() not in ['re', 'new']:
                raise ValueError("---Invalid input. Please enter 'Re' or 'New'.---")
                print("\n")
            break  # break out of the loop if input is valid
        except ValueError as e:
            print(e)
            print("\n")

    if check.lower() == 're':
        restock_laptop(dictt,order_laptops)
        #calling functions passing arguements and runs accordingly
        restock_laptop_bill(order_laptops)
    else:
        newstock_laptop(dictt,totallaptops)
        #calling functions passing arguements and runs accordingly    
        newstock_laptop_bill(totallaptops)

#this function asks user id and appends the data into 2d list and pass the list
def restock_laptop(dictt,order_laptops):
    #while loop for restocking items 
    print("\n")
    print("\t\t\t\t\t\t\t\t💻 Restocking Section for Shop 💻")
    laptopview()
    ch="y"
    while ch=="y":
        id = id_validation(dictt)
        #selected of laptop is stored in 'selected' list and printed without any brackets
        print("The Laptop you selected is : ",",".join(dictt[id]))
        print("Quantity Remaining : ",dictt[id][3])
        print("\n")
        while True:
            try:
                qnt = input("Enter the Quantity to ReStock: ")
                qnt = int(qnt) if qnt.isdigit() else -1
                if qnt <= 0:
                    raise ValueError("---Quantity must be a positive integer---")
                    print("\n")
                break  # break out of the loop if input is valid
            except ValueError as e:
                print(e)
                print("\n")

        print("\n")

        dictt[id][3] = str(int(dictt[id][3]) + qnt)
        
        #calling function to modify textfile
        modifieddict_to_txtfile(dictt)

        print("Your Order has been Placed")
        print("Updated Quantity : ",dictt[id][3])
        print("\n")

        #storing the laptops purchased in a 2D list
        nameoflaptop = dictt[id][0]
        brandoflaptop = dictt[id][1]
        priceoflaptop = dictt[id][2]
        quantityoflaptop = qnt
        processoroflaptop = dictt[id][4]
        graphicsoflaptop = dictt[id][5]
        ramoflaptop = dictt[id][6]
        memoryoflaptop = dictt[id][7]
        totalprice = int(priceoflaptop)*qnt  
        order_laptops.append([nameoflaptop, brandoflaptop, priceoflaptop, quantityoflaptop, processoroflaptop, graphicsoflaptop, ramoflaptop, memoryoflaptop, totalprice])
        
        #code if he wants to reenter
        while True:
            try:
                ch = input("Do you want to Restock another Laptop? (Y/N): ")
                if ch.upper() not in ["Y", "N"]:
                    raise ValueError("---Invalid input. Please enter 'Y' or 'N'.---")
                    print("\n")
                break  # break out of the loop if input is valid
            except ValueError as e:
                print(e)
                print("\n")
        print("\n")

def newstock_laptop(dictt,totallaptops):
    #empty 2D list to store the ordered laptop data
    ch="y"
    while ch == "y":
        nameoflaptop = input("Enter the Laptop Model : ")
        brandoflaptop = input("Enter the Laptop Brand : ")
        while True:
            try:
                priceoflaptop = int(input("Enter the Price(Nrs.): "))
                if priceoflaptop <= 0:
                    raise ValueError("---Price must be a positive integer---")
                    print("\n")
                break  # break out of the loop if input is valid
            except ValueError as e:
                print(e)
                print("\n")
        while True:
            try:
                quantityoflaptop = int(input("Enter the Quantity: "))
                if quantityoflaptop <= 0:
                    raise ValueError("---Quantity must be a positive integer---")
                    print("\n")
                break  # break out of the loop if input is valid
            except ValueError as e:
                print(e)
                print("\n")

        processoroflaptop = input("Enter the Processor : ")
        graphicsoflaptop = input("Enter the Graphics Card : ")
        ramoflaptop = input("Enter the RAM capacity : ")
        memoryoflaptop = input("Enter the Storage Capacity : ")
        totalprice = str(priceoflaptop * quantityoflaptop)
        # Create a list containing the input dictt to display the laptop details entered to the user
        new_laptop_dictt = [nameoflaptop, brandoflaptop, str(priceoflaptop), str(quantityoflaptop), processoroflaptop, graphicsoflaptop, ramoflaptop, memoryoflaptop]
        #Creating another list for bill and txt file bill
        laptop_dictt = [nameoflaptop, brandoflaptop, str(priceoflaptop), str(quantityoflaptop), processoroflaptop, graphicsoflaptop, ramoflaptop, memoryoflaptop,totalprice]
        #Storing it in 2D list
        totallaptops.append(laptop_dictt)

        # Add the new list to the dictt dictionary with a new key
        new_key = len(dictt) + 1
        dictt[new_key] = new_laptop_dictt

        #calling function to modify textfile
        modifieddict_to_txtfile(dictt)
    
        print("\n")
        print("The following dictt was entered : ",",".join(new_laptop_dictt))
        print("It was successfully added to the txt file.")
        print("\n")
        while True:
            try:
                ch = input("Do you want to Buy another Laptop? (Y/N): ")
                if ch.upper() not in ["Y", "N"]:
                    raise ValueError("---Invalid input. Please enter 'Y' or 'N'.---")
                break  # break out of the loop if input is valid
            except ValueError as e:
                print(e) 
                print("\n")
        print("\n")