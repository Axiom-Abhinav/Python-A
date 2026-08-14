import matplotlib.pyplot as plt

subjects = ["Subject 1","Subject 2","Subject 3","Subject 4","Subject 5","Subject 6","Subject 7"]


marks = []

for subject in subjects:
    mark = int(input(f"Enter marks for {subject}:"))
    marks.append(mark)


plt.figure(figsize=(8, 5))
plt.plot(subjects,marks, marker="o", color="Blue")

plt.title("Marks graph")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.ylim(0, 80)
plt.grid(True)

plt.show()

print(marks)