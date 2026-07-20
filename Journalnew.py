#Features:
# ====make sure you use this code on pc. it will not work on web.====
#you can open journal
#you can write journal
#you can remove journal
def start():
    print("=====Daily Journal=====")

    print("1. open journal")
    print("2. Write journal")
    print("3. Remove journal")
    print("4. Logout")



    while True:
        choice = input(str("choice:"))
        if choice == "2":
            file = open("Journal.txt", "a")
            journal = input("Write todays Journal: ")
            file.write(f"\n {journal}")
            file.close()

            exit_choice = input(str("Exit? Yes/No: "))
            if exit_choice == "yes" or exit_choice == "Yes":
                print("see you soon!")
                break

            elif exit_choice == "no" or exit_choice == "No":
                file = open("Journal.txt", "a")
                journal = input("Continue writing: ")
                file.write(f"\n{journal}")
                file.close()
                break

            else:
                print("Invalid Input")  

        elif choice == "1":
            file = open("Journal.txt", "r")
            lines = file.readlines()
            for all_files in range(len(lines)):
                print(f"{all_files + 1} {lines[all_files]}")
            file.close()
            break

        elif choice == "3":
            file = open("Journal.txt", "r")
            lines = file.readlines()
            for all_files in range(len(lines)):
                print(f"{all_files + 1} {lines[all_files]}")
            remove_lines = int(input("Which line you want to remove?: "))
            lines.pop(remove_lines-1)
            file = open("Journal.txt" , "w")
            for line in lines:
                file.write(line)
            file.close()
            print(f"successfully removed line {remove_lines}")

        elif choice == "4":
            break
        else:
            print("Invalid Input")


