#grading system
print("Enter five marks")
mrk1=int(input())
mrk2=int(input())
mrk3=int(input())
mrk4=int(input())
mrk5=int(input())

numberOFSub=5

sumOfMarks=(mrk1+mrk2+mrk3+mrk4+mrk5)
avg =sumOfMarks/numberOFSub

print(avg)

if(avg>=70 and avg<=100):
    print("A")
elif(avg >=60 and avg <= 69):
    print("B")
elif(avg >=50 and avg <= 59):
    print("C")
elif(avg >=40 and avg <= 49):
    print("D")
else:
    print("E")
    




