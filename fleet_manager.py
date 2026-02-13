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
    
    
    while True:
        new_id = input("Enter ID: ")
        if new_id in ids:
            print("This ID already exists.")
        else:
            break  #id is valid so break loop
    

    new_name = input("State name: ")
    
    
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
    
    
    if not names:
        print("No members found for removal.")
        return
    
    
    member_id = input("Enter ID you want removed: ")
    
    
    if member_id in ids:
        
        index = ids.index(member_id)
        removed_name = names[index]
        
    
        names.pop(index)
        ranks.pop(index)
        divisions.pop(index)
        ids.pop(index)
        
        print(f"{removed_name} (ID: {member_id}) has been removed from fleet records.")
    else:
        print(f"No member with this ID found: {member_id}")



def update_rank(names, ranks, ids):
    
    print("\n--- Update Crew Member Rank ---")
    
    
    if not names:
        print("No members to update.")
        return
    
    
    valid_ranks = ["Ensign", "Lieutenant Junior Grade", "Lieutenant", 
                   "Lieutenant Commander", "Commander", "Captain", "Admiral"]
    
    
    crew_id = input("Give ID details for update: ")
    
    
    if crew_id in ids:
    
        index = ids.index(crew_id)
        
    
        print(f"\nCurrent details:")
        print(f"Name: {names[index]}")
        print(f"Current Rank: {ranks[index]}")
        
        
        print("\nValid ranks: Ensign, Lieutenant Junior Grade, Lieutenant, Lieutenant Commander, Commander, Captain, Admiral")
        new_rank = input("Enter new rank: ").title()
        
        
        if new_rank in valid_ranks:
            
            ranks[index] = new_rank
            print(f"{names[index]} rank has been updated!")
            print(f"New rank: {new_rank}")
        else:
            print("Error: Invalid rank.Update unable to continue")
            
    else:
        print(f"ID: {crew_id}, is invalid")

def display_roster(names, ranks, divisions, ids):
    
    print("\n--- CREW ROSTER ---")
    
    if len(names) == 0:
        print("Zero members.")
        return
    
    for i in range(len(names)):
        print(names[i], ranks[i], divisions[i], ids[i]) 
    print(f"Number of crew members: {len(names)}") 


def search_crew(names, ranks, divisions, ids):
   
    print("\n--- Search Crew by Name ---")
    
    if len(names) == 0:
        print("No memebers in the fleet.")
        return
    
    search_term = input("Enter name you are searching for: ")
    found = False
    
    for i in range(len(names)):
        if search_term.lower() in names[i].lower():
            print(f"{names[i]} - {ranks[i]} - {divisions[i]} - ID: {ids[i]}")
            found = True
    
    if not found:
        print("Member not found.")


def filter_by_division(names, divisions):
   
    print("\n--- Filter by Division ---")
    
    if len(names) == 0:
        print("No memebers in the fleet.")
        return
    
    print("Divisions: Command, Operations, Sciences, Security")
    choice = input("Enter division: ")
    choice = choice.title()
    
    if choice != "Command" and choice != "Operations" and choice != "Sciences" and choice != "Security":
        print("Invalid division.")
        return
    
    print(f"\n{choice} Division:")
    found = False
    
    for i in range(len(names)):
        if divisions[i] == choice:
            print(f"  {names[i]}")
            found = True
    
    if not found:
        print("Not found.")