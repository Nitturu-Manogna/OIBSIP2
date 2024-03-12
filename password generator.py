import random
print('Hi!THis is password generator.')
#characters list
cap_letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
small_letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&','*','+','_','-',',','.',';',':','/','?']
#length of original password
length=int(input('enter the number of characters you want in password:'))
#no of each characters
c=int(input('enter the number of capital letters you want in password:'))
s=int(input('enter the number of small letters you want in password:'))
n=int(input('enter the number of numerics you want in password:'))
sy=int(input('enter the number of symbols you want in password:'))
#checking whether sum of characters is equal to original length of password
if length!=(c+s+n+sy):
    print('Determined characters length is not equal to original length of password')
else:
    password_list=[]
    for i in range(0,c):
        cap=random.choice(cap_letters)
        password_list+=cap
    for i in range(0,s):
        small=random.choice(small_letters)
        password_list+=small
    for i in range(0,c):
        num=random.choice(numbers)
        password_list+=num
    for i in range(0,c):
        sym=random.choice(symbols)
        password_list+=sym
random.shuffle(password_list)
password=""
#generating password
for i in password_list:
    password+=i
print('Your Password:',password)
