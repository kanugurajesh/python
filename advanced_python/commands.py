import argparse
import sys

# faulty calculator inputs you have to use 2+3 amd 2*3 and 2-5 and 2/1

def faulty_calculator(args):
    if args.z=='add':
        if args.x==2 and args.y==3:
            return 6
        else:
            return args.x + args.y
    elif args.z=='mul':
        if args.x==2 and args.y==3:
            return 7
        else:
            return args.x * args.y
    elif args.z=='div':
        if args.x==2 and args.y==1:
            return 3
        else:
            return args.x / args.y
    elif args.z=='sub':
        if args.x==2 and args.y==5:
            return -2
        else:
            return args.x - args.y
    else:
        return "sir your input is not valid"
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',type = float,default =0.0,help='sir you have type the input for furthur information you call command')
    parser.add_argument('--y',type = float,default = 1.0,help='sir please enter the operator you want to operate the inputs on')
    parser.add_argument('--z',type =str,default ='add',help='sir please enter the operator you want to operate the inputs on')
args = parser.parse_args()
sys.stdout.write(str(faulty_calculator(args)))