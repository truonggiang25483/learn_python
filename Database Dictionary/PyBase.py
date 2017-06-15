#PyBase
#DESC: User can select whether to Search, Add, Change or Delete and Entry in the DB
#Base Define#
live = 1
#While Loop#
while live == 1:
    dataRead = open("db.txt","r")
    if dataRead.read() !="" or dataRead.read() != "[]":
        dataRead.close()
        people = eval(open("db.txt","r").read())
        do = input("What do you wish to do?(search, add, change, delete):\n")
    else:
        people = []
        print("No Entries - Search, Change and Delete are not Available!")
        do = "add"

    #Search#
    if do == "search":
        c_name = input("Input the name of the person you are looking for:\n")
        def search(n):
            for p in people:
                if p['Name'] == n:
                     print("Name: "+ p['Name'])
                     print("Address: "+ p['Address'])
                     print("DOB: "+ p['DOB'])
                else:
                    print("Nobody with that name was found!")
                     

        search(c_name)

    ###Add##
    elif do == "add":
        print("#--------------------------Adding User--------------------------#")
        #Get New Data
        newName = input("Input the new name:\n")
        #Check exist#
        for p in people:
                if p['Name'] == newName:
                     print("Name is exist. Please try again!")
                else:
                    newAddress = input("Input the address:\n")
                    newDOB = input("Input the DOB:\n")
                    #Create a Temp Dict#
                    tempDict = {"Name": newName, "Address":newAddress,"DOB":newDOB}
                    people.append(tempDict)
                    #Write People to File#
                    dataWrite = open("db.txt","w")
                    dataWrite.write(str(people))
                    dataWrite.close()
                    print("Success - New Entry added to Database")

    #Change#
    elif do == "change":
        c_name = input("Input the name of the person you are looking for:\n")
        c = input("What do you wish to change ?(Address, DOB):\n")
        t = input("What do you wish to change it too?:\n")
        def change(n):
            for p in people:
                if p['Name'] == n:
                    p[c] = t
                    dataWrite = open("db.txt","w")
                    dataWrite.write(str(people))
                    dataWrite.close()                    
                    print("Success - Change Made!")
                else:
                    print("Change unsuccessful - Nobody with that name!")                   
        change(c_name)
        
    #Delete#
    elif do == "delete":
        c_name = input("Input the name of the person you are looking for:\n")
        start = eval(open("db.txt","r").read())

        def delete(n):
            cp = 0
            for p in people:
                if p['Name'] == n:
                    del people[cp]
                    dataWrite = open("db.txt","w")
                    dataWrite.write(str(people))
                    dataWrite.close()                    
                    print("Success - Entry Deleted!")
                cp = cp + 1
        if start == people:
            print("Delete Unsuccessful!")
            
        delete(c_name)

    #Wrong input#
    else:
        print("Invalid Operator. Please try again!")
        
    #Continue#
    if input("Continue?:\n") == "yes":
        live = 1
    else:
        if input("Print all Database Entries?:\n") == "yes":
            for p in people:
                print("Name: "+ p['Name'])
                print("Address: "+ p['Address'])
                print("DOB: "+ p['DOB'])
                print("\n")
                
        live = 0
