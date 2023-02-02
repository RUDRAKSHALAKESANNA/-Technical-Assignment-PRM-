size=int(input('enter the size of the list :'))
stringlist=[]
while len(stringlist)<size:
    elemnt=input('enter the string :')
    if len(elemnt)<2:
        print('length of string is less than two')
    else:
        stringlist.append(elemnt)
stringlist.sort(key=lambda x:x[-2])
print(stringlist)