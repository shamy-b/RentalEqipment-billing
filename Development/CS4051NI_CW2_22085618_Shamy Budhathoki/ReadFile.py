#function to read data from the file
def readData():
    file = open("Inventory.txt", "r") #opening inventory file
    data = [] #list to store data
    for line in file.readlines():
        row = line.replace("\n", "").split(",") #spliting the line after ,
        row[2] = int(row[2].replace("$", "")) #removing '$' symbol
        data.append(row) #adding data to the row
    file.close() #closing the file 
    return data #returning the list 