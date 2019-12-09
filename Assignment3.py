print('Enter 3 Data of any type\n')
names=[]
for data in range(3):
    names.append(input())
print('The data you have entered are'+str(names))
dataTobedeleted=input('Enter the name of the data you want to delete\n')
if dataTobedeleted in names:
    print(True)
else:
    print('Data not Found! Try Again')
indexOfdata=names.index(dataTobedeleted)
names.pop(indexOfdata)
print(names,'You have deleted',dataTobedeleted)


