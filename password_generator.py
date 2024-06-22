import  random
letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U' ,'V' , 'W' ,'X' ,'Y', 'Z']
symbol=['!','@', '#','$','%','^','&','*','+','-']
number=[ 0,1,2,3,4,5,6,7,8,9]
print("welcome")
nr_letter=int(input("how many letters do you want to include"))
nr_symbol=int(input("how many symbols do you want to include"))
nr_number=int(input("how many numers do you want to include"))
password=[]
for char in range(1,nr_letter + 1):
    random.choice(letter)
    password.append(random.choice(letter))

for sym in range(1,nr_symbol+1):
    random.choice(symbol)
    password.append(random.choice(symbol))
for num in range(1,nr_number+1):
    str (random.choice(number))
    password.append(random.choice(number))
print(password)
random.shuffle(password)
print(password)
pas=""
for yogesh in  password:
   pas+=str(yogesh)
print(f"your password is : {paso}")