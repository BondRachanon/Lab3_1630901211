Array1=["A","B","C","D","E","F"]
print(Array1)
Array_Length=len(Array1)
print("\nLength of stack :",Array_Length)
print(" ")
print("   ---FULL Stack----")
print("       AD    ST")
for i in range(len(Array1)):
    print("    [  "f"{i}", " ]", f"[ {Array1[i]}", "]")

#to reverse
#print("Reverse: ", end="")
#print(Array1.reverse())
Array1.pop(0)
Array1.pop(1)
Array1.pop(2)
Array1.pop()
Array1.pop()
Array1.pop()
print(" ")
print("     ----Pop STACK----")
print("       AD    ST")
for i in range(len(Array1)):
    print("    [  "f"{i}", " ]", f"[ {Array1[i]}", "]")

print(" ")
Array1.append('F')
Array1.append('E')
Array1.append('D')
Array1.append('C')
Array1.append('B')
Array1.append('A')
print("  ----Reverse STACK----")
print("       AD    ST")
for i in range(len(Array1)):
    print("    [  "f"{i}", " ]", f"[ {Array1[i]}", "]")
