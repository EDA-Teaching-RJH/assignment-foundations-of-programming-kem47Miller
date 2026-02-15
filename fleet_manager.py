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
    ids=["00","01","02","03","04"]
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
        print("8. Number of Leadership officers aboard")
        print("9. Exit")
        
        try:
            opt_picked =int(input(f"State your option (1-9),{student_login}: "))
            if 1 <= opt_picked <= 9:# if the input is 1 to 9
                return opt_picked#exit loop
            else:# if input not 1 to 9
                print("Mhmm...that's not right. Try picking a # 1 to  9.")#print this
        except ValueError:#if input not a number
            print("No. Pick a NUMBER from ONE to TEN.")#print this



def add_member(names, ranks, divisions, ids):
   
    # valid TNG ranks
    valid_ranks = ["Ensign", "Lieutenant Junior Grade", "Lieutenant", 
                   "Lieutenant Commander", "Commander", "Captain", 
                   "Admiral"]#looks better this way
    
    print("\n--- Add New Crew Member ---")
    
    
    while True:
        new_id = input("Enter ID: ").strip()
        if new_id in ids:
            print("Id entered MUST NOT already exist.")
        else:
            break  #id is valid so break loop
    

    new_name = input("State name: ")
    
    
    while True:
        
        print("\nValid ranks: Ensign, Lieutenant Junior Grade, Lieutenant, Lieutenant Commander, Commander, Captain,  Admiral")      
        new_rank = input("State rank: ").title()
        if new_rank in valid_ranks:
            break  # Rank is valid, exit loop
        else:
            print("Please enter one of the RANKS given ABOVE.")
    

    valid_divisions = ["Command", "Operations", "Sciences", "Security"
                       ]
    while True:
        print("\nValid divisions: Command, Operations, Sciences, " 
        "Security")
        new_division = input("State division: ").title()
        if new_division in valid_divisions:
            break
        else:
            print("Division entered DOES NOT EXIST.Choose a divisin from one given ABOVE!!")
    

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
    
    
    member_id = input("What is the id you want removed? ")
    
    
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
    
    print("\n--- Update Crew Member Rank ---")
    
    
    if not names:
        print("Sooo... no members for update.")
        return
    
    
    valid_ranks = [
        "Ensign", "Lieutenant Junior Grade",
       "Lieutenant", "Lieutenant Commander",
        "Commander", "Captain", "Admiral"
        ]
    
    
    staff_id = input("What information do you want revised? ")
    
    
    if staff_id in ids:
    
        index = ids.index(staff_id)
        
    
        print(f"\nCurrent details:")
        print(f"Name: {names[index]}")
        print(f"Current Rank: {ranks[index]}")
        
        
        print("\nValid ranks: Ensign, Lieutenant Junior Grade," " Lieutenant, Lieutenant Commander, Commander, Captain, Admiral")
        new_rank = input("State the rank: ").title()
        
        
        if new_rank in valid_ranks:
            
            ranks[index] = new_rank
            print(f"{names[index]} rank has been updated!")
            print(f"New rank: {new_rank}")
        else:
            print("Error: Invalid rank.Update unable to continue")
            
    else:
        print(f"ID: {staff_id}, is invalid")

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
'''def search_crew(names, ranks, divisions, ids):
   
    print("\n--- Search Crew by Name ---")
    
    if len(names) == 0:
        print("Yikes, no one is currently in the fleet.")
        return
    
    word = input("What name are you looking for? ")
    found = False
    
    for i in range(len(names)):
        if word.lower() in names[i].lower():
            print(f"{names[i]} - {ranks[i]} - {divisions[i]} - ID: {ids[i]}")
            found = True
    
    if not found:
        print("No such person found.")'''


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
'''def filter_by_division(names, divisions):
   
    print("\n--- Filter by Division ---")
    
    if len(names) == 0:
        print("Full Absence.")
        return
    
    print("Divisions: Command, Operations, Sciences, Security")
    div = input("Enter division: ")
    div = choice.title()
    
    match choice:
    case "Command" | "Operations" | "Sciences" | "Security":
        
        print(f"\n{choice} Division:")
        
    case _:
        print("Invalid division.")
        return
    #if choice != "Command" and choice != "Operations" and choice != "Sciences" and choice != "Security":
       # print("Invalid division.")
        #return
    
    print(f"\n{choice} Division:")
    found = False
    
    for i in range(len(names)):
        if divisions[i] == choice:
            print(f"  {names[i]}")
            found = True
    
    if not found:
        print("Not found.")'''


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
    
    print(f"Total payroll: {total} credits")
    return total




def count_officers(ranks):
    
    print("\n***** Number of Head Officers**")
    
    if len(ranks) == 0:
        print("The fleet is empty.")
        return 0
    
    count = 0
    
    for i in range(len(ranks)):
        if ranks[i] == "Captain":
            count = count + 1
        if ranks[i] == "Commander":
            count = count + 1
    
    print(f"Leading officers: {count}")
    return count
def main():
    
    print("\nFleet Manage Interface")
    

    names, ranks, divisions, ids = init_database()
    print("Booting up system")
    
    while True:
        choice = display_menu()
        
        if choice == 1:
            add_member(names, ranks, divisions, ids)
        elif choice == 2:
            remove_member(names, ranks, divisions, ids)
        elif choice == 3:
            update_rank(names, ranks, ids)
        elif choice == 4:
            display_roster(names, ranks, divisions, ids)
        elif choice == 5:
            search_crew(names, ranks, divisions, ids)
        elif choice == 6:
            filter_by_division(names, divisions)
        elif choice == 7:
            calculate_payroll(ranks)
        elif choice == 8:
            count_officers(ranks)
        elif choice == 9:
            break
        
        input("\nPress Enter to continue...")



main()