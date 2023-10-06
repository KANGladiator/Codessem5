import math
import string
import random

def check_prime(x):
    c=math.sqrt(x)
    n= math.ceil(c)
    for i in range (2,n):
        if x % i == 0:
            return 0
        else:
            continue
    return 1
    
  
x= (2**282589933)-1
res=check_prime(x)
if res==1:
    print("The number is prime")
else:
    print("number is not prime")


def gen_random_pass(min,max):
    lowercase=string.ascii_lowercase
    uppercase=string.ascii_uppercase
    digits=string.digits
    symbols = "!@#$%^&*()_-+=<>?/[]{}|"
    all_chars= lowercase+uppercase+digits+symbols
    pass_length= random.randint(min,max)
    password= ''.join(random.choice(all_chars) for _ in range(pass_length))
    return password
#print(gen_random_pass(8, 20))


            
    
    
