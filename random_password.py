import random
ab=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','1','2','3','4','5','6','7','9','0','`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','|',':',';','<',',','>','.','?','/']
len=int(input('Length of the Password  :'))
password=""
i=0
while i<=len:
    rc=random.choice(ab)
    password=password+rc
    i+=1
print(password)