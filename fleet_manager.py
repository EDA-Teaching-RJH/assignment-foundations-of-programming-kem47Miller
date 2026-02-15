def init_database():
    names=[
         "Jean-Luc Picard", 
         "William T. Riker",
           "Data", "Worf", 
           "Geordi La Forge"
           ]# easier to read
    ranks=[
        "Captain","Commander","Lieutenant Commander",
        "Lieutenant","Lieutenant Commander"
        ]
    divisions=[
        "Command", "Command", "Operations", "Security",
               "Operations"]
    ids=[11,10,9,8,7]
    return names, ranks,divisions, ids

def display_menu():
   student_login =input("State your full name: ")
   print(f"Hello {student_login},Loading Option menu now...")
   while True:#as long as True print this forever
        print("**YOUR OPTION MENU*****")
        print("1. Add crew member")
        print("2. Remove crew member")
        print("3. Update crew member rank")
        print("4. Display full roster")
        print("5. Search crew by name")
        print("6. Filter by division")
        print("7. Calculate payroll")
        print("8. Number of Leadering officers aboard")
        print("9. Exit")
        
        try:
            opt_picked =int(input(f"State your option (1-9),{student_login}: "))
            if 1 <= opt_picked <= 9:# if the input is 1 to 9
                return opt_picked#exit loop
            else:# if input not 1 to 9
                print("Mhmm...that's not right. Try picking a number 1 to  9.")#print this
        except ValueError:#if input not a number
            print("No. Pick a NUMBER from ONE to NINE.")#print this



def add_member(names, ranks, divisions, ids):
    valid_ranks = ["Ensign", "Lieutenant Junior Grade", "Lieutenant", 
                   "Lieutenant Commander", "Commander", "Captain", "Admiral"]
    
    print("\n--- Add New Crew Member ---")
    
    while True:
        try:
            new_id = int(input("Enter ID (integers only): ")) 
            if new_id <0:
                print("ID can't be a neagtive integer")
            elif new_id in ids:
                print("ID entered MUST NOT already exist.")
            else:
                break
        except ValueError:
            print("Please enter a NUMBER for ID.")
    
    
   

    new_name = input("State name: ").title()
    
    
    while True:
        
        print("\nValid ranks: Ensign, Lieutenant Junior Grade, Lieutenant, Lieutenant Commander, Commander, Captain,  Admiral")      
        new_rank = input("State rank: ").title()
        if new_rank in valid_ranks:
            break  # Rank is valid, exit loop
        else:
            print("Please enter one of the RANKS GIVEN ABOVE.")
    

    valid_divisions = ["Command", "Operations", "Sciences", "Security"
                       ]
    while True:
        print("\nValid divisions: Command, Operations, Sciences, " 
        "Security")
        new_division = input("State division: ").title()
        if new_division in valid_divisions:
            break
        else:
            print("Division entered DOES NOT EXIST.Choose a divs from one given ABOVE!!")
    

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
    
    try:
        member_id = int(input("What is the id you want removed? "))
    except ValueError:
        print("ID must be a number.")
        return
    
    if member_id in ids:
        index = ids.index(member_id)
        removed_name = names[index]
        
        names.pop(index)
        ranks.pop(index)
        divisions.pop(index)
        ids.pop(index)
        
        print(f"{removed_name} (ID: {member_id}) has been removed from fleet records.")
    else:
        print(f"oops:(----No member with this ID found: {member_id}")
       

def update_rank(names, ranks, ids):
    print("\n*** Update Crew Member Rank**")
    if len(names) == 0:
        print("No members")
        return
    
    valid_ranks = ["Ensign", "Lieutenant Junior Grade","Lieutenant", "Lieutenant Commander","Commander", "Captain", "Admiral"]
    
    try:
        staff_id = int(input("Please give staff id number? ")) 
    except ValueError:
        print("ID must be a number.")
        return
    
    if staff_id in ids:
        index = ids.index(staff_id)
        
        print(f"\nCurrent details:")
        print(f"Name: {names[index]}")
        print(f"Current Rank: {ranks[index]}")
        
        print("\nValid ranks: Ensign, Lieutenant Junior Grade, Lieutenant, Lieutenant Commander, Commander, Captain, Admiral")
        new_rank = input("State the rank: ").title()
        
        if new_rank in valid_ranks:
            ranks[index] = new_rank
            print(f"{names[index]} rank has been updated!")
            print(f"New rank: {new_rank}")
        else:
            print("An error has occured check information give is correct")
    else:
        print(f"{staff_id} does not work")    



def display_roster(names, ranks, divisions, ids):
    
    print("\n--- STAFF ROSTER ---")
    
    if len(names) == 0:
        print("Zero members.")
        return
    
    for i in range(len(names)):
        print(names[i], ranks[i], divisions[i], ids[i]) 
    print(f"Number of crew members: {len(names)}") 


def search_crew(names, ranks, divisions, ids):
    print("\n--- Search Crew by Name ---")
    
    if len(names) == 0:
        print("Yike, no one is currently in the fleet database.")
        return
    
    word = input("What name are you look for? ")
    count = 0  
    
    for i in range(len(names)):
        if word.lower() in names[i].lower():
            print(f"{names[i]} - {ranks[i]} - {divisions[i]} - ID: {ids[i]}")
            count += 1  
    
    if count == 0: 
        print("No such persons found.")
    else:
        print(f"Good news! There are {count} present.")



def filter_by_division(names, divisions):
    print("\n--- Filter by Division ---")
    
    if len(names) == 0:
        print("Full Absence.")
        return
    
    print("Divisions: Command, Operations, Sciences, Security")
    pick = input("Enter division: ")
    pick = pick.title()
    
    match pick:
        case "Command" | "Operations" | "Sciences" | "Security":
            print(f"\n{pick} Division:")# i feel match case works better here
            
            count = 0 
            for i in range(len(names)):
                if divisions[i] == pick:
                    print(f"  {names[i]}")
                    count += 1  
            
            if count == 0: 
                print("Not found.")
            else:
                print(f"Found {count} member(s)")
                
        case _:
            print("Try a division from the given.")
            return



def calculate_payroll(ranks):
   
    print("\n--- Calculate Payroll ---")
    
    if len(ranks) == 0:
        print("The fleet is empty.")
        return 0
    
    total = 0
    
    for i in range(len(ranks)):
        if ranks[i] == "Ensign":
            total = total + 200
        elif ranks[i] == "Lieutenant Junior Grade":
            total = total + 300
        elif ranks[i] == "Lieutenant":
            total = total + 400
        elif ranks[i] == "Lieutenant Commander":
            total = total + 550
        elif ranks[i] == "Commander":
            total = total + 750
        elif ranks[i] == "Captain":
            total = total + 1000
        elif ranks[i] == "Admiral":
            total = total + 1500
    
    print(f"Payment will be: {total} credits")
    return total




def count_officers(ranks):
    
    print("\n***** Number of Leading Officers**")
    
    if len(ranks) == 0:
        print("The fleet is empty.")
        return 0
    
    count = 0
    
    for i in range(len(ranks)):
        if ranks[i]=="Captain" or ranks[i]== "Commander":
            count += 1
    
    
    print(f"Number of Leading officers present: {count}")
    return count
def main():
    
    print("\nFleet Manage Interface")
    

    names, ranks, divisions, ids = init_database()
    print("***Booting up system*****")
    
    while True:
        opt_picked = display_menu()
        
        if opt_picked == 1:
            add_member(names, ranks, divisions, ids)
        elif opt_picked == 2:
            remove_member(names, ranks, divisions, ids)
        elif opt_picked == 3:
            update_rank(names, ranks, ids)
        elif opt_picked == 4:
            display_roster(names, ranks, divisions, ids)
        elif opt_picked == 5:
            search_crew(names, ranks, divisions, ids)
        elif opt_picked == 6:
            filter_by_division(names, divisions)
        elif opt_picked == 7:
            calculate_payroll(ranks)
        elif opt_picked == 8:
            count_officers(ranks)
        elif opt_picked == 9:
            break
        
        input("\nTo continue press the enter key...")



main()