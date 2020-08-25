n = int(input("Enter the value of n :"))
sum =0
a = 0
b = 1
count = 1
print("Fibonacci Series :" )
while(count<=n):
    print(sum)
    count += 1
    a = b
    b = sum
    sum = a + b
