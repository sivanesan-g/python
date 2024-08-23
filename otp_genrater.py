import random
otp=''
ran=['1','2','3','4','5','6','7','9','0']
i=1
while i<=6:
    pwd=random.choice(ran)
    otp=otp+pwd

    i+=1
print(' OTP is :',otp)

