import argparse
import sys
import math
parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=int)
args = parser.parse_args()
int_list = [args.principal, args.periods, args.interest, args.payment]
negs = 0
for num in int_list:
    if num:
        if num < 0:
            negs += 1
if len(sys.argv) < 5 or negs != 0:
    print("Incorrect parameters")
elif args.type != "annuity" and args.type != "diff":
    print("Incorrect parameters")
elif not args.interest:
    print("Incorrect parameters")
elif args.type == "diff" and args.payment:
    print("Incorrect parameters")
else:
    i = args.interest / (12 * 100)
    if not args.periods:
        n = math.ceil(math.log((args.payment / (args.payment - i * args.principal)), 1 + i))
        if n == 1:
            print("You need 1 month to repay this credit!")
        elif n < 12:
            print(f"You need {n} months to repay this credit!")
        elif n == 12:
            print("You need 1 year to repay this credit!")
        elif n == 13:
            print("You need 1 year and 1 month to repay this credit!")
        elif n // 12 == 1 and (n % 12) == 12:
            print(f"You need {(n // 12) + 1} years to repay this credit!")
        elif (n // 12) == 1:
             print(f"You need 1 year and {n % 12} months to repay this credit!")
        elif (n % 12) == 1:
            print(f"You need {n // 12} years and 1 month to repay this credit!")
        else:
            print(f"You need {n // 12} years and {n % 12} months to repay this credit!")
        print(f"Overpayment = {(args.payment * round(n) - args.principal)}")
    elif not args.payment  and args.type == "annuity":
        a = math.ceil(args.principal * ((i * ((1 + i) ** args.periods)) / (((1 + i) ** args.periods) - 1)))
        print(f"Your annuity payment = {a}!")
        print(f"Overpayment = {(a * args.periods - args.principal)}")
    elif not args.principal:
        p = math.ceil(args.payment / ((i * ((1 + i) ** args.periods)) / (((1 + i) ** args.periods) - 1)))
        print(f"Your credit principal = {p}!")
        print(f"Overpayment = {args.payment * args.periods - p}")
    elif args.type == "diff":
        pay_list = []
        for m in range(1, args.periods + 1):
            dm = (args.principal / args.periods) + i * (args.principal - (args.principal * (m - 1)) / args.periods)
            dm = math.ceil(dm)
            pay_list.append(dm)
            print(f"Month {m}: paid out {dm}")
        print(f"Overpayment = {sum(pay_list) - args.principal}")
