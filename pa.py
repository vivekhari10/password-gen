import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']

print("------Welcome to Password Generator------")
nr_letters=int(input("How many letters would you like in your paassword?\n"))
nr_symbols=int(input("How many symbols would you like?\n"))
nr_numbers=int(input("How many numbers would you like?\n"))
password=""


for char in range(1,nr_letters+1):
   random_char= random.choice(letters)
   password=password+random_char
for char in range(1,nr_symbols+1):
    password+=random.choice(symbols)
for char in range(1,nr_numbers+1):
    password+=random.choice(numbers)
print(password)
