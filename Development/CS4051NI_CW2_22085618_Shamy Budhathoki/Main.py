#importing all neccessary files 
import ReadFile
import Operation
import WriteFile
import Message

#creating main function 
def main():
    data = ReadFile.readData() # Reading data from the file
    Message.display_welcome_message() # Displaying welcome message 
    option=0
    
    # loop for main menu while condition is true
    while True:
        Message.display_option_message()#displaying option table
        #Using try except for exception handling
        try:
            option = int(input(" "*25+" Please select a serial number from the options [1, 2,3 or 4] : "))#Giving option to the user 
        except ValueError:
            print("\n"+"---"*41)
            print(" "*41+"Invalid input!!! please enter a valid Number")
            print("---"*41+"\n")
        print("\n"+"---"*41+"\n"*2)
        if 0 <= option > 4:    #to make sure given S.N is correct
            print("\n"+"---"*41)
            print(" "*35+"Invalid input.Please enter a value from 1 to 4")
            print("---"*41+"\n")
            continue
        
        # when customer selects option 1
        if option == 1:
            print("───"*41)
            print(" "*53+"Invoice to")
            print("───"*41+"\n")
            #Getting customer information
            customer_name = input("Enter the name of the customer Renting : ")
            address=input("Enter your address : ")
            #Using try except for exception handling
            try:
                phone_number=int(input("Enter the Phone number: "))
            except ValueError:
                print("\n"+"───"*41)
                print(" "*41+"Invalid input!!! please enter a valid Number")
                print("───"*41+"\n")
                continue
            email_address= input("Enter your Email-address : ")
            print("\n"+"---"*41+"\n"*2)
            Operation.displayData(data)# Displaying available items for rent 
            total_amount = 0
            total_quantity = 0
            store = [] #creating list to store row and quantity
            
            # loop for rent while condition is true 
            while True:  
                #Using try except for exception handling
                try:
                    row = int(input("\n"+"1. Enter the S.N to Rent from : "))
                except ValueError:
                    print("\n"+"───"*41)
                    print(" "*41+"Invalid input!!! please enter a valid Number")
                    print("───"*41+"\n")
                    continue
                #Checks if the selected S.N is valid or not 
                if 1 <= row <= len(data):
                    #Using try except for exception handling
                    try:
                        quantity = int(input("2. Enter the quantity to Rent : "))
                    except ValueError:
                        print("\n"+"───"*41)
                        print(" "*41+"Invalid input!!! please enter a valid Number")
                        print("───"*41+"\n")
                        continue
                    available_quantity = int(data[row - 1][3])
                    #Checks if the selected quantity is valid or not
                    if 1 <= quantity <= available_quantity:
                        store.append((row, quantity))#adding it in store list 
                        item = data[row - 1]
                        action = 'Rent'
                        total_amount += item[2] * quantity #calculating total amount
                        total_quantity += quantity
                        #generating rental invoice 
                        rent_invoice = Message.generate_rental_invoice( customer_name, action, total_amount, quantity, store, data,phone_number,address,email_address)
                        data = Operation.update_Data(data, row, quantity)#updating data for rented quantity
                        WriteFile.write_Transaction_rent(rent_invoice, customer_name) #writting transaction detail to the file
                        WriteFile.write_Data(data)#writting updated data to the inventory
                            
                    else:
                        #Displaying information to invalid quantity
                        print("───"*41)
                        print(" "*52+"Invalid Quantity")
                        print("───"*41+"\n")
                        print(" "*35+"Insufficient stock!!! Please enter a valid stock." + "\n" +" "*35+ "Available quantity:", available_quantity)
                else:
                    #Displaying information to invalid S.N
                    print("\n"+"---"*41+"\n"+" "*30+"Invalid S.N. Please enter a valid S.N from the table."+"\n"+"---"*41+"\n")
                print("\n"+"---"*41)  
                #ending the loop if user dont want to rent items  
                ask = input(" "*20+"Do you wish to continue Renting? Type 'y' for yes and 'n' for no: ")
                print("---"*41)
                if ask.lower() == 'n' or ask.lower() == 'no':
                    print("\n"+"───"*41)
                    print(" "*41+"Your Invoice has been generated")
                    print("───"*41+"\n")
                    break  
                   
        # when customer selects option 2
        elif option == 2:
            #List to  store returning items
            returned_items = []
            returned_quantities = []
            fine_amounts = [] 
            rental_durations = []
            print("───"*41)
            print(" "*53+"Invoice to")
            print("───"*41+"\n")
            #Getting customer information
            customer_name = input("Enter the name of the customer Returning : ")
            address=input("Enter your address : ")
            #Using try except for exception handling
            try:
                phone_number=int(input("Enter the Phone number: "))
            except ValueError:
                print("\n"+"───"*41)
                print(" "*41+"Invalid input!!! please enter a valid Number")
                print("───"*41+"\n")
                continue
            email_address= input("Enter your Email-address : ")
            print("\n"+"---"*41+"\n"*2)
            Operation.displayData(data)# Displaying available items for rent 
            isTrue = True
            
            # loop for return while condition is true 
            while isTrue:
                #Using try except for exception handling
                try:
                    row = int(input("\n"+"1. Enter the S.N to Return from : "))
                except ValueError:
                    print("\n"+"───"*41)
                    print(" "*41+"Invalid input!!! please enter a valid Number")
                    print("───"*41+"\n")
                    continue
                #Checks if the selected S.N is valid or not 
                if 1 <= row <= len(data):
                    #Using try except for exception handling
                    try:
                        returned_quantity = int(input("2. Enter the quantity to Return : "))#getting information for returning items
                    except ValueError:
                        print("\n"+"───"*41)
                        print(" "*41+"Invalid input!!! please enter a valid Number")
                        print("───"*41+"\n")
                        continue
                    #Using try except for exception handling
                    try:
                        rental_duration = int(input("3. Please enter Your rental duration [in days]: "))
                    except ValueError:
                        print("\n"+"───"*41)
                        print(" "*41+"Invalid input!!! please enter a valid Number")
                        print("───"*41+"\n")
                        continue
                    item = data[row - 1]
                    returned_items.append((item, row))#Adding item and row inside returned item list
                    returned_quantities.append(returned_quantity)#Adding returned_quantity inside returned_quantities list
                    rental_durations.append(rental_duration)#Adding rental_duration inside rental_durations list
                    fine_per_day = int(item[2])

                    rental_days = 5
                    late_days = rental_duration - rental_days#Late days calculation
                    fine_amount = late_days * fine_per_day #Calculating fine amount if fined
                    fine_amounts.append(fine_amount)#Adding fine amount in fine amount list 
                    action = 'Return'
                    #generating return invoice 
                    return_invoice = Message.generate_return_invoice(returned_items, customer_name, action, returned_quantities, fine_amounts, phone_number, rental_durations,address,email_address)
                    data = Operation.update_Data(data, row, -returned_quantity)#updating data for renturned quantity
                    WriteFile.write_Transaction_return(return_invoice, customer_name)#writting transaction detail to the file
                    WriteFile.write_Data(data)#writting updated data to the inventory
                else:
                    #Displaying information to invalid S.N
                    print("\n"+"---"*41+"\n"+" "*30+"Invalid S.N. Please enter a valid S.N from the table."+"\n"+"---"*41+"\n")
                print("\n"+"---"*41)
                print("\n"+"---"*41)  
                #ending the loop if user dont want to rent items  
                ask = input(" "*20+"Do you wish to continue Renturning? Type 'y' for yes and 'n' for no: ")
                print("---"*41)
                #ending the loop if user dont want to renturn items
                if ask.lower() == 'n' or ask.lower() == 'no':
                    print("\n"+"───"*41)
                    print(" "*41+"Your Invoice has been generated")
                    print("───"*41+"\n")
                    isTrue = False
                    print("---"*41)
                           
        elif option == 3:
            #Displaying Equipment inventory 
            Operation.displayData(data)
        
        elif option == 4:
            #Showing exit message to the user 
            Message.display_exit_message()
            break

# calling main function         
main()
