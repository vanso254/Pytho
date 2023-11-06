# for i in range(10):
#     print(i)

# carlist= ["Volvo","Tesla","Ford"]

# for car in carlist:
#     print(car)

# for i in range(1,10):
#     for k in range(1,10):
#         print(i,k)

# for i in range(1,200):
#     is_prime=True
#     for k in range(1,int(i**0.5)+1):
#         if i%k==0:
#             is_prime=False
#             break
        
#     if is_prime:
#         print (i)

for num in range(1, 200):  # We start from 2, as 1 is not a prime number.
    is_prime = True
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num)
