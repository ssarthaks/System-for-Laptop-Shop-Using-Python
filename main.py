#importing other python files for the workflow
import read
import write
import operations

write.CUIheading()
while True:
    write.CUI_every_executions()
    user_input = read.get_user_choice()
    if user_input == "1":
        read.laptopview()
        print("\n")
        input("---Press Enter to Continue---")
    elif user_input == "2":
        operations.orderlaptop()
        input("---Press Enter to Continue---")
    elif user_input == "3":
        operations.updatestorelaptops()
        print("\n")
        input("---Press Enter to Continue---")
    elif user_input == "4":
        write.exit()
    else:
        print("\t\t\t\t\t\t 💻 Invalid Input! Please Input Valid Option and Try Again! 💻")
        input("---Enter to Continue---")