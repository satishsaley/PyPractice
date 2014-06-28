##public static int getParity(long n) {
##		// TODO Auto-generated method stub
##		
##		int p=0;
##		while(n!=0){
##			p = p^1;
##			n=n&(n-1);
##		}
##		
##		
##		return p%2;
##	}
import sys

def get_parity(num):
    p = 0
    while num!=0:
        p=p^1   
        num=num&(num-1)
    return p
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print(get_parity(int(test)))