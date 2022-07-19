import csv

def updateRecepies()
myList = ["1","2","3","4"]

testDict = [{"Name":"myTest","Ingredients":",".join(str(elem) for elem in myList),"Webpage":"strona"}]

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name','Ingredients','Webpage']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerows(testDict)