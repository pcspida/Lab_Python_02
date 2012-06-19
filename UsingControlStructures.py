# Solution for Q:5
theInput = raw_input("Enter an integer: ")
theInput = int(theInput)
if theInput%2 == 0:
    print "You entered an even number"
else:
    print "You entered an odd number"

print "------------------------------"

# Solution for Q:6
primarySchoolAge = 4
legalVotingAge = 18
minimumPresidentAge  = 44
retirementAge = 60
personsAge = input("Enger an age: ")
personsAge = int(personsAge)
if personsAge < primarySchoolAge:
    print "Too young."
else:
    if personsAge > legalVotingAge:
        print "Remember to vote"
    if personsAge > minimumPresidentAge:
        print " Vote for me"
    elif personsAge < minimumPresidentAge:
            print "You can't be president"
    if personsAge >= retirementAge:
        print "Too old."
print "--------------------------------------"

# Solution for Q:7
x=40
while x>=0:
    if x%3==0:
        print x
    x=x-1
print "--------------------------------------"

# Solution for Q:8
for x in range(6,30):
    if x%2==0 or x%5==0 or x%5==0:
        ""
    else:
        print x
print "--------------------------------------"

# Solution for Q:9
n=1
while (79*n)%97!=1:
    n=n+1
print n
print "--------------------------------------"
