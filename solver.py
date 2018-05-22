#!/usr/bin/env python

""" Quadratic Equation Solver """

import sys
import time
import numbers

import sympy


def main():
    #----------------introduce program---------------------------
    print("\n")
    print("QUADRATIC EQUATION SOLVER".center(65, "~"), "\n")
    print("This program solves Quadratic Equations of form: "
            "ax² + bx + c.\n")
    time.sleep(1)
    #--------------sympy pretty printing instructions-----------
    sympy.init_printing(use_latex=True)
    #----------------ask for inputs and process------------------
    while True:
        a, b, c = None, None, None
        while not isinstance(a, numbers.Integral):
            a = validate(input("enter the value of a: "))
        while not isinstance(b, numbers.Integral):
            b = validate(input("enter the value of b: "))
        while not isinstance(c, numbers.Integral):
            c = validate(input("enter the value of c: "))

        s1 = "+" if b >= 0 else ""   # append `+` sign if b >= 0
        s2 = "+" if c >= 0 else ""   # append `+` sign if c >= 0
        while True:
            print()
            resp = input(
                    "Compute solution(s) for %dx² %s%dx %s%d = 0 ? "
                    "[y/n]: " % (a, s1, b, s2, c)).lower()
            if resp in ("o", "y", "n"):
                break

        if resp == "n":
            while True:
                quit = input("Do you wish to quit ? [y/n]: ")
                if quit.lower() in ("o", "y", "n"):
                    break
            if quit in ("o", "y"):  # user wish to quit
                print("Goodbye!")
                sys.exit(0)         # exit program

        # process user's inputs
        s = [x for x in solve(a, b, c) if x != None]
        # append "s" to `solution` if there are more than one found
        suffix = "" if len(s) < 1 else "s"
        end = ":" if len(s) > 0 else "."

        print("(%d) solution%s found%s\n" % (len(s), suffix, end))
        if len(s) == 1:
            sympy.pprint(s[0])
        elif len(s) > 1:
                sympy.pprint((s[0], s[1]))

        print()

        #----------------ask for another equation-------------------
        while True:
            resp = input("Do you wish to solve another one ? [y/n]: ")
            if resp.lower() in ("o", "y"):
                print()
                break
            if resp == "n":
                print("Goodbye!")
                sys.exit(0)   # exit program
    #-------------------end of main()-------------------------------


def solve(a, b, c):
    """ Determine x valid value(s) for any Quadratic Equation
    `ax² + bx + c = 0` where a, b, c are known values.
    Returns a tuple of solutions (x1, x2)."""

    if a == 0:
        if b == 0:
            return (None, None)
        return (sympy.Rational(-c, b),None)

    d = b**2 - (4*a*c)  # discriminant
    if d < 0:
        return (None, None)
    if d == 0:
        return (sympy.Rational(-b, 2*a), None)
    if d > 0:
        sqrt_d = sympy.sqrt(d)
        x1 = (-b + sqrt_d) / (2*a)
        x2 = (-b - sqrt_d) / (2*a)
        return (x1, x2)

def validate(string):
    """Return int(string) if string can be represented as an integer.
    Otherwise, re-return string unmodified.
    By the way, it also output an error message to the user."""
    try:
        return int(string)
    except ValueError:
        print("\nError: invalid value -> %s\n" % string)
        return string


if __name__ == "__main__":
    main()
