import Operation

#function for displaying option table to the customer
def display_option_message():
    print("\n"+"───"*41)
    print(" "*43+"Event Equipment Rental shop")
    print("───"*41+"\n")
    print("""          
            │────────────────────────────────────────────────────────────────────────────────────────────│
            │     S.N     │                                 Options                                      │
            │────────────────────────────────────────────────────────────────────────────────────────────│
            │      1.     │                       Rent items from the store                              │
            │             │                                                                              │
            │      2.     │                       Return rented items from the store                     │
            │             │                                                                              │
            │      3.     │                       Display available items                                │
            │             │                                                                              │  
            │      4.     │                       Exit the System                                        │
            │────────────────────────────────────────────────────────────────────────────────────────────│
          
    """)
    
#functionn to show welcome message
def display_welcome_message():
    print("\n"+"---"*41)
    print(" "*54+"!!!!Welcome!!!!")
    print("---"*41+"\n")
    print(" "*3+"Use of our services for planning of your event.Renting equipment is simple,transaction bills are givem to the customer")
    print(" "*3+"immediately,managing stock is easy and efficient.Rent, Return back and enjoy your event with our products!!")
    print("\n"+"---"*41)

#functionn to show exit message    
def display_exit_message():
    print("\n"+"---"*41)
    print(" "*56+"!!!!Thank You!!!!")
    print("---"*41+"\n")
    print(" "*35+"Thank you for choosiing our services.Please visit Again")
    print("\n"+"---"*41)
   
#function to generate rental invoice for the customer 
def generate_rental_invoice(customer_name, action, total_amount, quantity, store, data,phone_number,address,email_address):
    invoice = (
        "--"*62+"\n"+
        " "*50+"Event Equipment Shop\n"+
        "--"*62+"\n"+
        "\n"+"BILLING DETAILS : "+" "*69+"RENTAL INVOICE : "+"\n"*2+
        "Customer : " + customer_name + " "*62+ "Rental date: " + Operation.function_time()+"\n"+
        "Address : "+str(address)+" "*70+"Action : " + action +"\n"
        "Phone Number : "+str(phone_number)+"\n" 
        "Email Address : "+str(email_address)+"\n"*2 +
        "----"*31)
    #adding heading to the table
    invoice+=("\n"+"|"+" "+"S.N"+" "*5+"|"+" "*3+"Equipment"+" "*29+"|"+" "*3+"Brand"+" "*24+"|"+" "*3+"Price"+" "*10+"|"+" "*2+"Quantity"+" "*8+"|"+"\n")
    invoice+="----"*31+"\n"
    
    sn = 1  
    #looping rented items to show in invoice
    for items in store:
        row = items[0] 
        quantity = items[1]  
        item_info = data[row - 1]
        invoice += (
            "|" + " " + str(sn) + " " * (8 - len(str(sn))) +
            "|" + " " +  item_info[0] + " " * (40 - len(item_info[0])) +
            "|" + " " +  item_info[1] + " " * (31 - len(item_info[1])) +
            "|" + " " + "$" + str(item_info[2] * quantity) + " " * (17 - len("$" + str(item_info[2] * quantity))) +
            "|" + " " + str(quantity) + " " * (16 - len(str(quantity))) + " " + "|\n"
        )
        sn += 1  #Increasing serial number
    #adding ending line
    invoice+="----"*31+"\n"*2
     
    #Adding total amount and showing contact information    
    invoice += (
        "  "*44+"Total Amount : $" + str(total_amount) + "\n"*4+
        "QUESTIONS?"+"\n"*2+
        "Email us at eventrentalshop@gmail.com or Contact Us at 01-994869 "+"\n"*3+
        " "*48+"THANK YOU FOR YOUR BUSINESS"+"\n"*2+  
        "--"*62
    )
    return invoice

#function to generate return invoice for the customer
def generate_return_invoice(items, customer_name, action, returned_quantities, fine_amounts, phone_number, rental_durations,address,email_address):
    invoice = (
        "--"*62+"\n"+
        " "*50+"Event Equipment Shop\n"+
        "--"*62+"\n"+
        "\n"+"BILLING DETAILS : "+" "*69+"RENTURN INVOICE : "+"\n"*2+
        "Customer : " + customer_name + " "*62+ "Renturn date: " + Operation.function_time()+"\n"+
        "Address : "+str(address)+" "*70+"Action : " + action +"\n"
        "Phone Number : "+str(phone_number)+"\n" 
        "Email Address : "+str(email_address)+"\n"*2 +
        "----"*31)
    #adding heading to the table
    invoice += ("\n"+"|"+" "+"S.N"+" "*3+"|"+" "*3+"Equipment"+" "*27+"|"+" "*3+"Brand"+" " *14+"|"+" "*3+"Returned Quantity"+" "*5+"|"+" "*3+"Rental Duration"+" "*7 +"|" + "\n")
    invoice += "----"*31 + "\n"

    total_fine = 0
    #looping renturned items to show in invoice
    for index in range(len(items)):
        item, row = items[index]  
        returned_quantity = returned_quantities[index]  
        fine_amount = fine_amounts[index]
        total_fine += fine_amount
        rental_duration = rental_durations[index]
        invoice += (
            "|" + " " + str(index + 1) + " " * (6 - len(str(index + 1))) + 
            "|" + " " + item[0] + " " * (38 - len(item[0])) +
            "|" + " " + item[1] + " " * (21 - len(item[1])) +
            "|" + " " + str(returned_quantity) + " " * (24 - len(str(returned_quantity))) +
            "|" + " " + str(rental_duration) + " days" + " " * (19 - len(str(rental_duration))) + "|" + "\n"
        )
    #adding ending line    
    invoice += "----"*31 + "\n"*2
    
    #adding contact information and  total fine
    if total_fine > 0:
        invoice += (
            "  "*44+"Fine Amount : $" + str(total_fine) + " " * (17 - len(str(total_fine))) + "\n"*4+
            "QUESTIONS?"+"\n"*2+
            "Email us at eventrentalshop@gmail.com or Contact Us at 01-994869 "+"\n"*3+
            " "*47+"THANK YOU FOR YOUR BUSINESS"+"\n"*2+  
            "--"*62
        )
    else:
        #adding fine amount
        invoice += "  "*44+"Fine Amount : $0" + " " * 14 + "\n"*4+"QUESTIONS?"+"\n"*2+"Email us at eventrentalshop@gmail.com or Contact Us at 01-994869 "+"\n"*3+" "*48+"THANK YOU FOR YOUR BUSINESS"+"\n"*2+ "--"*62
                    
    return invoice
    