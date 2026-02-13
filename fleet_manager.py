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



def add_member(names, ranks, divisions, ids):
   
    # valid TNG ranks
    valid_ranks = ["Ensign", "Lieutenant Junior Grade", "Lieutenant", 
                   "Lieutenant Commander", "Commander", "Captain", "Admiral"]
    
    print("\n--- Add New Crew Member ---")
    
    # STEP 1: checking if id is UNIQUE
    while True:
        new_id = input("Enter ID: ")
        if new_id in ids:
            print("This ID already exists.")
        else:
            break  #id is valid so break loop
    

    new_name = input("State name: ")
    
    # STEP 3: Validate RANK is valid TNG rank
    while True:
        
        print("\nValid ranks: Ensign, Lieutenant Junior Grade, Lieutenant, Lieutenant Commander, Commander, Captain,  Admiral")      
        new_rank = input("State rank: ").title()
        if new_rank in valid_ranks:
            break  # Rank is valid, exit loop
        else:
            print("Please try again.")
    

    valid_divisions = ["Command", "Operations", "Sciences", "Security"]
    while True:
        print("\nValid divisions: Command, Operations, Sciences, Security")
        new_division = input("Enter division: ").title()
        if new_division in valid_divisions:
            break
        else:
            print("Invalid Division.")
    

    names.append(new_name)
    ranks.append(new_rank)
    divisions.append(new_division)
    ids.append(new_id)
    
    print(f"{new_name} has been added to fleet records")

def remove_member(names, ranks, divisions, ids):
    
    print("\n--- Remove Crew Member ---")
    
    # Check if fleet is empty
    if not names:
        print("The fleet is empty. No members to remove.")
        return
    
    # Ask for ID
    member_id = input("Enter the ID of the crew member to remove: ")
    
    # Check if ID exists
    if member_id in ids:
        # Find the index position
        index = ids.index(member_id)
        removed_name = names[index]
        
        # Remove from ALL 4 lists at the SAME index
        names.pop(index)
        ranks.pop(index)
        divisions.pop(index)
        ids.pop(index)
        
        print(f"{removed_name} (ID: {member_id}) has been removed from the fleet.")
    else:
        print(f"No crew member found with ID: {member_id}")