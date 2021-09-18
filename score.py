s = input("Enter Score: ")
score = float(s)
print(score)

if score > 100 or score < 0:
    print("score input out of range")
elif score >= 95:
    print("A")
elif score >= 85:
    print("B")
elif score >= 75:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
