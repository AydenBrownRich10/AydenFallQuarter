numGrade=int(input("Enter your # grade "))

if(numGrade>=90):
    print("you have an A")
elif (80<=numGrade<=89):
    print("you have a B")
elif (70<=numGrade<=79):
    print("you have a C")
elif(60<=numGrade<=69):
    print("you have a D, better luck next time")
elif(numGrade<60):
    print("you have a F, your a  failer")