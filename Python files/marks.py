subjects = ["Subject 1","Subject 2","Subject 3","Subject 4","Subject 5","Subject 6","Subject 7"]


marks = []

for subject in subjects:
    mark = int(input(f"Enter marks for {subject}: "))
    marks.append(mark)

Average = sum(marks) / len(marks)

print("Average:", Average)

if Average >70 and Average <=80:
    print("Your Grade is A+")

elif Average >60 and Average <=70:
    print("Your Grade is A")
    
elif Average >50 and Average <=60:
    print("Your Grade is B+")

elif Average >40 and Average <=50:
    print("Your Grade is B")

elif Average >30 and Average <=40:
    print("Your Grade is C")

elif Average >20 and Average <=30:
    print("Your Grade is D")

elif Average >=0 and Average <=20:
    print("Your Grade is F")

else:
    print("end")
