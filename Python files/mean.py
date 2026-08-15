nums = []

total = int(input("Enter the total number of numbers: "))

for i in range(total):
    num = int(input(f"Enter number {i + 1}: "))
    nums.append(num)

mean = sum(nums) / total

print("Numbers:", nums)
print("Mean =", mean)