def init_database():
    names=[ "Jean-Luc Picard", "William T. Riker", "Data", "Worf", "Geordi La Forge" ]
    ranks=["Captain","Commander","Lieutenant Commander","Lieutenant","Lieutenant Commander"]
    divisions=["Command", "Command", "Operations", "Security","Operations"]
    ids=["00","01","02","03","04"]
    return names, ranks,divisions,ids

def display_menu():
   student_login =input("State your full name: ")
   print(f"Hello {student_login},Loading Option menu now...")
   while True:#as long as True print this forever
        print("----OPTION MENU----")
        print("1. Add crew member")
        print("2. Remove crew member")
        print("3. Update crew member rank")
        print("4. Display full roster")
        print("5. Search crew by name")
        print("6. Filter by division")
        print("7. Calculate payroll")
        print("8. Count senior officers")
        print("9. Exit")
        
        try:
            choice = int(input(f"State your option (1-9), {student_login}: "))
            if 1 <= choice <= 9:# if the input is 1 to 9
                return choice#exit loop
            else:# if input not 1 to 9
                print("Enter a number 1 to  9.")#print this
        except ValueError:#if input not a number
            print("Enter a number 1 to 9.")#print this
