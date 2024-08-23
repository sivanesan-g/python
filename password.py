ab=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','1','2','3','4','5','6','7','9','0']
b1=['1','2','3']
name=input('Enter the Password file name:')
fi=open(f"{name}.txt","w")
fi.close()
file=open(f"{name}.txt","a")
st=0

size =int(input("Enter length of password:"))
for a1 in ab:
    if size<=1:
        s=a1
        st=st+1
        file.write(f'''{s}
''')
        
    else:
        for a2 in ab:
            if size<=2:
                s=a1+a2
                st=st+1
                file.write(f'''{s}
''')
            else:
                for a3 in ab:
                    if size<=3:
                        s=a1+a2+a3
                        st=st+1
                        file.write(f'''{s}
''')
                    else:
                        for a4 in ab:
                            if size<=4:
                                s=a1+a2+a3+a4
                                st=st+1
                                file.write(f'''{s}
''')
                            else:
                                for a5 in ab:
                                    if size<=5:
                                        s=a1+a2+a3+a4+a5
                                        st=st+1
                                        file.write(f'''{s}
''')
                                    else:
                                        for a6 in ab:
                                            if size<=6:
                                                s=a1+a2+a3+a4+a5+a6
                                                st=st+1
                                                file.write(f'''{s}
''')
                                            else:
                                                for a7 in ab:
                                                    if size<=7:
                                                        s=a1+a2+a3+a4+a5+a6+a7
                                                        st=st+1
                                                        file.write(f'''{s}
''')
                                                    else:
                                                        for a8 in ab:
                                                            if size<=8:
                                                                s=a1+a2+a3+a4+a5+a6+a7+a8
                                                                st=st+1
                                                                file.write(f'''{s}
''')
                                                            else:
                                                                for a9 in ab:
                                                                    if size<=9:
                                                                        s=s=a1+a2+a3+a4+a5+a6+a7+a8+a9
                                                                        st=st+1
                                                                        file.write(f'''{s}
''')
                                                                    else:
                                                                        for a10 in ab:
                                                                            if size<=10:
                                                                                s=s=a1+a2+a3+a4+a5+a6+a7+a8+a9+a10
                                                                                st=st+1
                                                                                file.write(f'''{s}
''')
                                                                            else:
                                                                                for a11 in ab:
                                                                                    if size<=11:
                                                                                        st=st+1
                                                                                        s=s=a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11
                                                                                        file.write(f'''{s}
''')
                                                                                    else:
                                                                                        for a12 in ab:
                                                                                            if size<=12:
                                                                                                st=st+1
                                                                                                s=s=a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12
                                                                                                file.write(f'''{s}
''')
                                                                                            else:
                                                                                                for a13 in ab:
                                                                                                    if size<=13:
                                                                                                        st=st+1
                                                                                                        s=s=a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13
                                                                                                        file.write(f'''{s}
''')
                                                                                                    else:
                                                                                                        for a14 in ab:
                                                                                                            if size<=14:
                                                                                                                st=st+1
                                                                                                                s=s=a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14
                                                                                                                file.write(f'''{s}
''')
                                                                                                            else:
                                                                                                                for a15 in ab:
                                                                                                                    if size<=15:
                                                                                                                        st=st+1
                                                                                                                        s=s=a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15
                                                                                                                        file.write(f'''{s}
''')
                                                                                                                    else:
                                                                                                                        for a16 in ab:
                                                                                                                            if size<=16:
                                                                                                                                st=st+1
                                                                                                                                s=s=a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15+a16
                                                                                                                                file.write(f'''{s}
''')
print(f"{st} password  genrate complite....")
        


