
print('''
      1 --> read
      2 --> write''')
usr=int(input("enter  :"))
if usr==2:
    admin=str(input("Enter the admin user name :"))
    pwd=str(input("Enter the password        :"))
    o=open("adminuser.txt",'r')
    a=[]
    
    if admin=='admin' and pwd=='pass':
        
        a=open("data.txt",'a')

        
        while True:
            name=input('Enter Name      :')
            dep= input('Enter Number    :')                
            a.write(f"""
{name}\t\t\t\t\t{dep}
-------------------------------------------------""")
                
                
                
            print("data is added..")
            en=input('exit-->1 or enter contine')
            if en=='exit' or en=='EXIT'or en=='1':
                break
                
        a.close()

                        
            
            

    else:
        print("Admin Only allow to write....")
elif usr==1:
    s=open("data.txt",'r')
    v=input('Enter the name or number :')
    print('''
*************************************************
* NAME                                  NUMBER  *
*************************************************''')
    
    for l in s:
        
        if v in l:
            print('''
-------------------------------------------------''')
            print(l)
    else:
        print('given name or number not in data')
else:
    print("Enter currect value.....")