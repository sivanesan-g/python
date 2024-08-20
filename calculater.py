import math
green='\033[01;32m'
red = '\033[01;31m'
blue= '\033[01;34m'
gr='\033[01;35m'

while True:
    ipt=input(f"{blue}expresstion  : {green}")
    ans=eval(ipt)
    print(f"{gr}answer       :{green}",ans)
