import Operation

#function to write data in inventory file
def write_Data(data):
    file = open("Inventory.txt", "w") #opening inventory file 
    for row in data:
        changed_row = [] #list to store new row
        #looping through each value in row
        for index in range(len(row)):
            item = row[index] 
            #adding '$'symbol to the third column           
            if index == 2:
                changed_row.append('$' + str(item))
            else:
                changed_row.append(str(item))       
        file.write(",".join(changed_row) + "\n") #writing new row to the file 
    file.close() #closing the file 

#function for writting rental transaction infromation
def write_Transaction_rent(rent_invoice, customer_name):
    times=str(Operation.file_time()) #getting date time 
    #showing transaction file name
    transaction_file_name = customer_name+"_" +"Rent"+"_"+times+ "_" +"transaction.txt"
    file = open(transaction_file_name, "w") #opening transaction file to write
    file.write(rent_invoice + "\n") #Writting rental invoice in the file
    file.close() #closing the file 

#function for writting renturn transaction infromation
def write_Transaction_return(return_invoice, customer_name):
    times=str(Operation.file_time()) #getting date time 
    #showing transaction file name
    transaction_file_name =  customer_name+"_" +"Return"+"_"+times+ "_" +"transaction.txt"
    file = open(transaction_file_name, "w") #opening transaction file to write
    file.write(return_invoice + "\n") #Writting rental invoice in the file
    file.close() #closing the file 



