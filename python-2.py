def oddseries(a):
    result = []
    for i in range(a):
        num = 2 * i + 1
        result.append(num)
    print("Output:", ", ".join(map(str, result)))
a = int(input("Enter the number of odd numbers to print: "))
if a <= 0:
    print("Please enter a positive integer.")
else:
    oddseries(a)
