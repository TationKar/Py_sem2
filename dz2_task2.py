# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.
print("\n")
n = int(input("Введите число N = ",))
i=2
multi = i*i
while multi < n:
    print(f"degtwo = {multi}")
    multi *=i