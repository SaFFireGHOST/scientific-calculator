#!/usr/bin/env python3
import argparse
from calculator import sqrt, factorial, ln, power

def interactive():
    menu = """\nScientific Calculator
1) sqrt(x)
2) factorial(x)
3) ln(x)
4) x^b
5) exit
"""
    while True:
        print(menu)
        c = input("choice: ").strip()
        try:
            if c == "1":
                x = float(input("x: "))
                print("=>", sqrt(x))
            elif c == "2":
                x = int(input("x (non-negative int): "))
                print("=>", factorial(x))
            elif c == "3":
                x = float(input("x (>0): "))
                print("=>", ln(x))
            elif c == "4":
                x = float(input("x: "))
                b = float(input("b: "))
                print("=>", power(x, b))
            elif c == "5":
                break
            else:
                print("Invalid choice")
        except Exception as e:
            print("Error:", e)

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--op", choices=["sqrt","fact","ln","pow"], help="operation")
    parser.add_argument("--x", type=float, help="x value")
    parser.add_argument("--b", type=float, help="b value (for pow)")
    args = parser.parse_args()
    if not args.op:
        interactive()
    else:
        if args.op == "sqrt":
            print(sqrt(args.x))
        elif args.op == "fact":
            print(factorial(int(args.x)))
        elif args.op == "ln":
            print(ln(args.x))
        elif args.op == "pow":
            print(power(args.x, args.b))

if __name__ == "__main__":
    cli()
