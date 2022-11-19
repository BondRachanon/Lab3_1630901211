Array1 = ["A", "B", "C", "D", "E", "F"]
print(Array1)
Array_Length = len(Array1)
print("\nLength of stack :", Array_Length)
print(" ")
print(" FULL Stack")
print("    AD    ST")
for i in range(len(Array1)):
    print("|   "f"{i}", "  |", f"{Array1[i]}", "|")
Array1.pop(3)  # Popตำแหน่งที่3
print(" ")
print("  ----Pop----")
print("    AD    ST")
for i in range(len(Array1)):
    print("|   "f"{i}", "  |", f"{Array1[i]}", "|")
