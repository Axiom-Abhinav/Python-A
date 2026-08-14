import matplotlib.pyplot as plt

n = int(input("Enter number:"))

seqeunce = [n]

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

    seqeunce.append(n)

plt.figure(figsize=(8, 5))
plt.plot(seqeunce, marker="o", color="blue")

plt.title("Collatz Conjecture")
plt.xlabel("Step")
plt.ylabel("Value")
plt.grid(True)

plt.show()
print(seqeunce)