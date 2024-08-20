import random
green='\033[01;32m'
red = '\033[01;31m'
blue= '\033[01;34m'
gr='\033[01;35m'
#com=random.choices(["stone","paper","siccssor"])
com=random.choices([1,2,3])
print(com)
while True:
    print(f''' {gr}
          1 --> stone
          2 --> paper
          3 --> siccssor
          ''')
    user=int(input("your choice :"))
    if user in [1,2,3]:
        break
    

st ="stone"
ppr='paper'
sis="siccssor"
if com[0]==1:
    print("computer :",st)
elif com[0]==2:
    print("computer :",ppr)
elif com[0]==3:
    print("computer :",sis)
if com[0] == user:
    print(f'''{blue}
          
██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗
██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║
██║░░██║██████╔╝███████║░╚██╗████╗██╔╝
██║░░██║██╔══██╗██╔══██║░░████╔═████║░
██████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░ 
          ''')
elif (com[0]==1 and user==3) or (com[0]==2 and user==1) or (com[0]==3 and user==2):
    print(f'''{red}
          
█▀▀ █▀▀█ █▀▄▀█ █▀█ █░█ ▀█▀ █▀▀ █▀█
█▄▄ █  █ █░▀░█ █▀▀ █▄█ ░█░ ██▄ █▀▄
    ▀▀▀▀
           █░█░█ █ █▄░█
           ▀▄▀▄▀ █ █░▀█
          ''')
    
    
else:
    print(f'''{green}
╭╮╱╱╭╮
┃╰╮╭╯┃
╰╮╰╯╭┻━┳╮╭┳━╮╭━━┳━┳━━╮╭╮╭╮╭┳┳━╮
╱╰╮╭┫╭╮┃┃┃┃╭╯┃╭╮┃╭┫┃━┫┃╰╯╰╯┣┫╭╮╮
╱╱┃┃┃╰╯┃╰╯┃┃╱┃╭╮┃┃┃┃━┫╰╮╭╮╭┫┃┃┃┃
╱╱╰╯╰━━┻━━┻╯╱╰╯╰┻╯╰━━╯╱╰╯╰╯╰┻╯╰╯
          ''')
          
