#this functioon gets the user input value and sends it to main function
def get_user_choice():
    print("\n")
    user_input=input("Which Option Would You Like to Choose ? (1-4) : ")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    return user_input

#this function displays all the available laptops
def laptopview():
    #reading data from txt file
    file = open("LaptopDetails.txt","r")
    print("\n")
    print("The available Laptops are Displayed Below:")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("ID \tLaptopName \t\tBrand\t      Price(NRS)     Quantity \t\tProcessor\t\tGraphics \t\tRAM     \tMemory")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    lines=file.readlines()
    a=1
    for line in lines:
        print(a,"\t"+line.replace(",","\t\t"))
        a = a + 1
    file.close()
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")

#function to read txt file and store data into dictionary
def mydict():
    id=1
    lapdict={}
    file = open("LaptopDetails.txt","r")
    for line in file:
        line = line.replace("\n","")
        lapdict.update({id : line.split(",")})
        id = id + 1
    return lapdict