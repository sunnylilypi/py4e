s = input("Enter Score: ")
score = float(s)
print(score)

if score > 1.0 or score < 0:
    print("score input out of range")
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")