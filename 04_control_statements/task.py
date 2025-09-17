# Tasks to work

# -> Sum of First N Natural Numbers
#     -> Take a number n from the user and print the sum of first n natural numbers.
#     -> input is 3 then output should be 6 (1+2+3)
#     -> input is 10 then output should be 55 (1+2+3+...+10)


# -> Print numbers from 1 to 20 but skip multiples of 3
#     -> Output: 1 2 4 5 7 8 10 11 13 14 16 17 19 20

# -> Prime Number Check
#     -> Write a program to check if a number is prime or not

n = int(input("enter a natural number: "))
if n>=1:
    total = 0
    for n in range(1,n+1):
        total += n
    print(f"total is {total}")
    # range(n)
    # for n in range(1,n+1):
    #     print(n)
else:
    print("it is not a natural")

a = int(input("enter a number: "))
for a in range(1,a+1):
    if a%3 == 0:
        continue
    print(a)

#prime numbers
num = int(input("Enter a number: "))
if num <=1:
    print("its not a prime number ")
else:
    is_prime = True
    for i in range(2,num) :
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")











