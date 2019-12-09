print('Enter four names')
theNames=[]
for name in range(0,4):
    theNames.append(input())
print('The name that is longest is\n')
print(max(theNames,key=len))



