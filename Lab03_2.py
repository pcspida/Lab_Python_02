number=input("Enter number to send: ")
numberTemp=number
changeNumber=0
x=0
finalReverse=0
while numberTemp>0:
    digit=numberTemp%10
    changeNumber=((digit+7)%10)*(10**x)+ changeNumber
    numberTemp=numberTemp/10
    
    finalReverse=(finalReverse*10)+changeNumber/(10**x)
    x=x+1
    
print "Encryption process:" ,number , "==>" ,changeNumber ,"==>" , finalReverse 
