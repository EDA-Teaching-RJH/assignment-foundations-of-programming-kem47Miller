n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:
        print("Loading module " + str(loading))
        loading += 1 #3 added 'loading += 1' so load will eventually = 5 and wont be stuck print loading module 0 
        
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        if opt == "1": #2change = to ==, not assigning opt to 1 but do an equality check  
            print("Current Crew List:")
            
            for i in range(len(n)):#4change range(10) to the number of items in list (only 4 crew memebers not 10)
                print(n[i] + " - " + r[i]) 
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name)
            r.append(new_rank)#5added so that new ranks can be added because in sync/added append so parallel lists are nsync /have same length/have same number of members and have them in correct order
            d.append(new_div)#5added so that new divisions can be added 'cause in sync
            print("Crew member added.")
            
        elif opt == "3":
            rem = input("Name to remove: ")
            if rem in n:#6thchange- 'if rem in n:' addedd so code can first check to see if name given is on the list and if so remove name.before, code would break if name giben not on list, now it dont.
                idx = n.index(rem)
                n.pop(idx)
                r.pop(idx)
                d.pop(idx)
                print("Removed.")
            else:
                print("No such member is present")    
           
            
        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain" or rank== "Commander": #7th added 'rank==' to Commander to make comparison true for not just the captain but for the commander too.
                    count = count + 1
            print("High ranking officers: " + str(count))#8th added str().python cant add string to integer so crash happen. i need to make integer string to prevent this.
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        elif len(n) == 0:#9elif replace the if that was here.before the 2 if statement were about the same thing/checking same condition- len(n). elif is used here instead to remain precise and prevent error.
            print("Database empty.")

        
        fuel = 100
        consumption = -100#10replace 0 with -100
        while fuel > 0:
            
            print("Idling...")
            fuel=consumption #10replace break with fuel so in code the fuel decreases.orginally it didnt and the break prevent the the loop from running continuously but by making this addition the orginal intent can be carried out and code is not broken.
            
        print("End of cycle.")

run_system_monolith() #1added () so function is called and code can run
