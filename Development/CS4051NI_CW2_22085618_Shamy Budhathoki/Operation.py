import datetime

#function to display equipment inventory 
def displayData(data):
    print("───"*41)
    print(" "*48+"Equipment Inventory")
    print("───"*41+"\n")
    #heading for the table
    print("───"*41)
    print("│"+" "+"S.N"+" "*5+"│"+" "*3+"Equipment"+" "*29+"│"+" "*3+"Brand"+" "*24+"│"+" "*3+"Price"+" "*10+"│"+" "*2+"Stock"+" "*10+"│")
    print("───"*41)
    #looping data to print each item
    for item_num in range(len(data)):
        row = data[item_num]
        sn = item_num + 1  
        #Showing all information 
        print("│ " + " " + str(sn) + " " * (7 - len(str(sn))) +
              "│ " + " " + row[0] + " " * (39 - len(row[0])) +
              "│ " + " " + row[1] + " " * (30 - len(row[1])) +
              "│ " + " $" + str(row[2]) + " " * (16 - len("$" + str(row[2]))) +
              "│ " + " " + row[3] + " " * (15 - len(row[3])) +"│")
    print("───"*41)

    
#function to display updated data
def update_Data(data, row, quantity):
    data[row - 1][3] = str(int(data[row - 1][3]) - quantity) #updating quantity value of a row
    return data

#to show datetime function in rent and return invoices
def function_time():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    
    final_time = year + "-" + month + "-" + day + "/" + hour + ":" + minute #to show the date time in a format

    return final_time

#to show datetime function in the file name
def file_time():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    
    file_time = str(year  + month  + day  + hour  + minute )#converting to string to show it in file 

    return file_time


