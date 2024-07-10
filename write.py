import os
import random
#functions of the program that does task accordingly
def CUIheading():
    # Entrance of the website is coded here
    #heading of application
    print("💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻")
    print("\n")
    print("\t\t\t\t\t\t\t\t PROCESSOR PALACE PVT. LTD.")
    print("\n")
    print("\t\t\t\t\t\t\t\t   📍Kalanki, Kathmandu")
    print("\n")
    print("\t\t\t\t\t\t\t\t    📞 +977-9860688334")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    #welcome message to the user
    print("\t\t\t\t\t\t\t 💻 !!!Welcome to the World of Laptops!!! 💻")
    print("\n")
    print("\t\t\t\t\t 💻 We hope you find what you're looking for and that you enjoy your stay.💻")
    
#function for designing
def CUI_every_executions():
    #input is asked for the user to enter and run the program accordingly
    #options for the user are displayed here
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻")
    print("\n")
    print("1. Preview Available Laptops")
    #print("\n")
    print("2. Buy Yourself a New Laptop(Sales)")
    #print("\n")
    print("3. For Store to Update Stock(Purchase)")
    #print("\n")
    print("4. System Exit")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻")
   
#function that writes the values of dictionary to txt file after laptop is purchased by user
def modifieddict_to_txtfile(dictt):
    #these lines of code writes the dictionary into the textfile and the textfile is updated with reduced quantity
    file = open("LaptopDetails.txt","w")
    num_lines = len(dictt)  # count the number of lines to write
    for i, (key, values) in enumerate(dictt.items()):
        line = ','.join(values)
        file.write(line)
        if i < num_lines - 1:
            file.write('\n')  # write newline character for all lines except the last
    file.close()

#function for bill generator for the user in console when user buys                                                                                                                                                   
def user_order_bill(dictt,user_laptops,shipcost,name,address,phone):
    vat = 0
    vatableamt = 0
    totalamt = 0
    #creating a bill for the user
    #GUI part for the bill
    print("\n")
    print("Here Is Your Bill : ")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("\t\t\t\t\t\t\t\t PROCESSOR PALACE PVT. LTD.")
    print("\n")
    print("\t\t\t\t\t\t\t\t   📍Kalanki, Kathmandu")
    print("\n")
    print("\t\t\t\t\t\t\t\t    📞 +977-9860688334")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("\t\t\t\t\t\t\t\t\tTAX INVOICE")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    #importing date and time from library
    from datetime import date
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Date : ",date.today())
    print("Customer Name : ",name)
    print("\n")
    print("Address : ",address)
    print("\n")
    print("Phone No. : ",phone)
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("SN.\t\t\tParticular \t\t\t\t\t\t      Quantity \t\t      Amount(Per Pc.) \t\t       Total Amt(Each)")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    #using loop to extract each data from the 2D list where the laptop details of the user is stored
    a=1
    for each in user_laptops:
        print(a,"\t",each[0],",",each[1],",",each[4],",",each[5],",",each[6],",",each[7],"\t\t\t",each[3],"\t\t\tNRS.",each[2],"\t\t\tNRS.",each[8])
        a=a+1
    taxableamt = totalamt + shipcost
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    #using loop for calculating the total amount of all the laptops that user bought
    for i in user_laptops:
        vatableamt=vatableamt+i[8]
    vat = 13/100 * vatableamt
    totalamt = vatableamt + vat
    print("\t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Shipping Amount = Nrs.",shipcost,"/-")
    print("\n")
    print("\t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Net Amount = Nrs.",vatableamt,"/-")
    print("\n")
    print("\t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    VAT(13%) = Nrs.",vat,"/-")
    print("\n")
    print("\t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Gross Amount = Nrs.",totalamt,"/-")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")

    #BILL IN NEW TXT FILE EVERY ITERATION
    #math.random function to print unique file names
    from datetime import date
    # Generate a random number between 1000 and 9999
    used_numbers = set()  # keep track of used numbers
    while True:
        random_num = random.randint(1000, 9999)
        if random_num not in used_numbers:
            used_numbers.add(random_num)
            file_name = f"{random_num}_{name}_Bill.txt"
            if not os.path.exists(file_name):
                break
    #opens new bill every iteration
    f = open(file_name,"w")
    f.write("Here is your Bill :")
    f.write("\n")
    f.write("------------------------------------------------------------------------------------------------------------------------------")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t   PROCESSOR PALACE PVT. LTD.")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t\t Kalanki, Kathmandu")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t\t  +977-9860688334")
    f.write("\n")
    f.write("------------------------------------------------------------------------------------------------------------------------------")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Date : ")
    f.write(str(date.today()))
    f.write("\n")
    f.write("Customer Name : ")
    f.write(name)
    f.write("\n")
    f.write("Address : ")
    f.write(address)
    f.write("\n")
    f.write("Phone No : ")
    f.write(phone)
    f.write("\n")
    f.write("------------------------------------------------------------------------------------------------------------------------------")
    f.write("\n")
    f.write("SN.\t\t\tParticular \t\t\t\t\t\t    Quantity \t     Amount(Per Pc.) \t     Total Amt(Each)")
    f.write("\n")
    f.write("------------------------------------------------------------------------------------------------------------------------------")
    for i, laptop in enumerate(user_laptops):
        f.write(f"\n{i+1}\t{laptop[0]},{laptop[1]},{laptop[4]},{laptop[5]},{laptop[6]},{laptop[7]}\t\t\t{laptop[3]}\t\t\tNrs.{laptop[2]}\t\t\tNrs.{laptop[8]}")
    f.write("\n")
    f.write("------------------------------------------------------------------------------------------------------------------------------")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Shipping Amount = ")
    f.write(str(shipcost))
    f.write("/-")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Net Amount = ")
    f.write(str(vatableamt)) 
    f.write("/-")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    VAT(13%) = ")
    f.write(str(vat)) 
    f.write("/-")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Gross Amount = ")
    f.write(str(totalamt)) 
    f.write("/-")
    f.write("\n")
    f.write("------------------------------------------------------------------------------------------------------------------------------")
    f.close()

#this function shows bill of the laptop that has been restocked
def restock_laptop_bill(order_laptops):
    #Code to print the bill
    totalamt_novat = 0
    vat = 0
    totalamt = 0
    print("\n")
    print("Here is your Bill : ")
    print("\n")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("\t\t\t\t\t\t\t\t LAPTOP SANSAAR PVT. LTD.")
    print("\n")
    print("\t\t\t\t\t\t\t\t   📍Baluwatar, Kathmandu")
    print("\n")
    print("\t\t\t\t\t\t\t\t    📞 +977-9851153586")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("\t\t\t\t\t\t\t\t\tTAX INVOICE")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")

    #importing date and time from library
    from datetime import date
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Date : ",date.today())
    print("Customer Name : PROCESSOR PALACE PVT. LTD.")
    print("\n")
    print("Address : Kalanki")
    print("\n")
    print("Phone No. : 9860688334")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("SN.\t\t\tParticular \t\t\t\t\t\t      Quantity \t\t      Amount(Per Pc.) \t\t       Total Amt(Each)")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    
    #using loop to extract each data from the 2D list where the laptop dictt of the user is stored
    a=1
    for each in order_laptops:
        print(a,"\t",each[0],",",each[1],",",each[4],",",each[5],",",each[6],",",each[7],"\t\t\t",each[3],"\t\t\tNRS.",each[2],"\t\t\tNRS.",each[8])
        a=a+1
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")

    #using loop for calculating the total amount of all the laptops that user bought
    for i in order_laptops:
        totalamt_novat=totalamt_novat+i[8]
    vat = 13/100 * totalamt_novat
    totalamt = totalamt_novat + vat
    print("\t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   Net Amount = Nrs.",totalamt_novat,"/-")
    print("\n")
    print("\t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   VAT(13%) = Nrs.",vat,"/-")
    print("\n")
    print("\t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   Gross Amount = Nrs.",totalamt,"/-")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")

    #code to print the bill to a new txt file every time
    #BILL IN NEW TXT FILE EVERY ITERATION
    #math.random function to print unique file names
    
    from datetime import date
    # Generate a random number between 1000 and 9999
    used_numbers = set()  # keep track of used numbers
    while True:
        random_num = random.randint(1000, 9999)
        if random_num not in used_numbers:
            used_numbers.add(random_num)
            file_name = f"{random_num}_ProcessorPalace_AddQuantityBill.txt"
            if not os.path.exists(file_name):
                break
    #opens new bill every iteration
    f = open(file_name,"w")
    
    f.write("Here is your Bill :")
    f.write("\n")
    f.write("------------------------------------------------------------------------------------------------------------------------------")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t\tLAPTOP SANSAAR PVT. LTD.")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t\t Baluwatar, Kathmandu")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t\t  +977-9851153486")
    f.write("\n")
    f.write("------------------------------------------------------------------------------------------------------------------------------")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Date : ")
    f.write(str(date.today()))
    f.write("\n")
    f.write("Customer Name : Processor Palace PVT. LTD.")
    f.write("\n")
    f.write("Address : Kalanki")
    f.write("\n")
    f.write("Phone No : 9860688334")
    f.write("\n")
    f.write("------------------------------------------------------------------------------------------------------------------------------")
    f.write("\n")
    f.write("SN.\t\t\tParticular \t\t\t\t\t\t    Quantity \t     Amount(Per Pc.) \t     Total Amt(Each)")
    f.write("\n")
    f.write("------------------------------------------------------------------------------------------------------------------------------")
    for i, laptop in enumerate(order_laptops):
        f.write(f"\n{i+1}\t{laptop[0]},{laptop[1]},{laptop[4]},{laptop[5]},{laptop[6]},{laptop[7]}\t\t\t{laptop[3]}\t\t\tNrs.{laptop[2]}\t\t\tNrs.{laptop[8]}")

    f.write("\n")
    f.write("------------------------------------------------------------------------------------------------------------------------------")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Net Amount = Nrs.")
    f.write(str(totalamt_novat))
    f.write("/-")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    VAT(13%) = Nrs.")
    f.write(str(vat)) 
    f.write("/-")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Gross Amount = Nrs.")
    f.write(str(totalamt)) 
    f.write("/-")
    f.write("\n")
    f.write("------------------------------------------------------------------------------------------------------------------------------")
    f.close()

def newstock_laptop_bill(totallaptops):
    #Code to print the bill
    vat = 0
    totalamt_novat = 0
    totalamt = 0 
    print("Here is your Bill : ")
    print("\n")
    input("--Enter to Generate Bill--")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("\t\t\t\t\t\t\t\t\t LAPTOP SANSAAR PVT. LTD.")
    print("\n")
    print("\t\t\t\t\t\t\t\t   📍Baluwatar, Kathmandu")
    print("\n")
    print("\t\t\t\t\t\t\t\t    📞 +977-9851153586")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("\t\t\t\t\t\t\t\t\tTAX INVOICE")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")

    #importing date and time from library
    from datetime import date
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Date : ",date.today())
    print("Customer Name : PROCESSOR PALACE PVT. LTD.")
    print("\n")
    print("Address : Kalanki")
    print("\n")
    print("Phone No. : 9860688334")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("SN.\t\t\tParticular \t\t\t\t\t\t      Quantity \t\t      Amount(Per Pc.) \t\t       Total Amt(Each)")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
        
    #using loop to extract each data from the 2D list where the laptop dictt of the user is stored
    a=1
    for each in totallaptops:
        print(a,"\t",each[0],",",each[1],",",each[4],",",each[5],",",each[6],",",each[7],"\t\t\t",each[3],"\t\t\tNRS.",each[2],"\t\t\tNRS.",each[8])
        a=a+1
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")

    #using loop for calculating the total amount of all the laptops that user bought
    for i in totallaptops:
        totalamt_novat=totalamt_novat+int(i[8])
    vat = 13/100 * totalamt_novat
    totalamt = totalamt_novat + vat
    print("\t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   Net Amount = Nrs.",totalamt_novat,"/-")
    print("\n")
    print("\t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   VAT(13%) = Nrs.",vat,"/-")
    print("\n")
    print("\t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   Gross Amount = Nrs.",totalamt,"/-")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    #code to print the bill to a new txt file every time
    #BILL IN NEW TXT FILE EVERY ITERATION
    #math.random function to print unique file names
    from datetime import date
    # Generate a random number between 1 and 10000
    random_num = random.randint(1000, 9999)
    file_name = f"{random_num}_ProcessorPalace_NewLaptopBill.txt"
    #opens new bill every iteration
    f = open(file_name,"w")
    f.write("Here is your Bill :")
    f.write("\n")
    f.write("------------------------------------------------------------------------------------------------------------------------------")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t\tLAPTOP SANSAAR PVT. LTD.")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t\t Baluwatar, Kathmandu")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t\t  +977-9851153486")
    f.write("\n")
    f.write("------------------------------------------------------------------------------------------------------------------------------")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Date : ")
    f.write(str(date.today()))
    f.write("\n")
    f.write("Customer Name : Processor Palace PVT. LTD.")
    f.write("\n")
    f.write("Address : Kalanki")
    f.write("\n")
    f.write("Phone No : 9860688334")
    f.write("\n")
    f.write("------------------------------------------------------------------------------------------------------------------------------")
    f.write("\n")
    f.write("SN.\t\t\tParticular \t\t\t\t\t\t    Quantity \t     Amount(Per Pc.) \t     Total Amt(Each)")
    f.write("\n")
    f.write("------------------------------------------------------------------------------------------------------------------------------")
    a=1
    for i, laptop in enumerate(totallaptops):
        f.write(f"\n{i+1}\t{laptop[0]},{laptop[1]},{laptop[4]},{laptop[5]},{laptop[6]},{laptop[7]}\t\t\t{laptop[3]}\t\t\tNrs.{laptop[2]}\t\t\tNrs.{laptop[8]}")
    
    f.write("\n")
    f.write("------------------------------------------------------------------------------------------------------------------------------")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Net Amount = Nrs.")
    f.write(str(totalamt_novat))
    f.write("/-")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    VAT(13%) = Nrs.")
    f.write(str(vat)) 
    f.write("/-")
    f.write("\n")
    f.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    Gross Amount = Nrs.")
    f.write(str(totalamt)) 
    f.write("/-")
    f.write("\n")
    f.write("------------------------------------------------------------------------------------------------------------------------------")
    f.close()

#this function exits the program 
def exit():
    print("\n")
    print("\t\t\t\t\t\t\t\t 💻 Thank You for Visiting Our Store! 💻")
    print("\n")
    print("💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    quit()