"""
=========================================================
Python f-Strings (Formatted String Literals)
=========================================================

This file demonstrates:

1. Basic variable interpolation
2. Expressions
3. Function calls
4. Number formatting
5. Alignment
6. Padding
7. Floating point precision
8. Percentage formatting
9. Thousands separators
10. Binary / Octal / Hex
11. Dates
12. Debug syntax (Python 3.8+)
13. Conversion flags
14. Escaping braces
15. Multiline f-strings

Run:

    python f_string_demo.py
"""

from datetime import datetime

print("=" * 60)
print("1. Basic Variables")
print("=" * 60)

name = "Alice"
age = 25

print(f"Name: {name}")
print(f"Age : {age}")


print("\n" + "=" * 60)
print("2. Expressions")
print("=" * 60)

a = 10
b = 3

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} ** {b} = {a ** b}")


print("\n" + "=" * 60)
print("3. Calling Functions")
print("=" * 60)

text = "python"

print(f"Upper : {text.upper()}")
print(f"Length: {len(text)}")


print("\n" + "=" * 60)
print("4. Floating Point Precision")
print("=" * 60)

pi = 3.14159265358979

print(f"Default : {pi}")
print(f"2 digits: {pi:.2f}")
print(f"4 digits: {pi:.4f}")
print(f"8 digits: {pi:.8f}")


print("\n" + "=" * 60)
print("5. Percentage")
print("=" * 60)

score = 0.87654

print(f"Default   : {score}")
print(f"Percentage: {score:.2%}")


print("\n" + "=" * 60)
print("6. Thousands Separator")
print("=" * 60)

money = 9876543210

print(f"{money}")
print(f"{money:,}")


print("\n" + "=" * 60)
print("7. Width and Alignment")
print("=" * 60)

word = "Python"

print(f"|{word:<15}|  Left")
print(f"|{word:^15}|  Center")
print(f"|{word:>15}|  Right")


print("\n" + "=" * 60)
print("8. Padding")
print("=" * 60)

number = 42

print(f"{number:05}")
print(f"{number:010}")


print("\n" + "=" * 60)
print("9. Binary / Octal / Hex")
print("=" * 60)

n = 255

print(f"Decimal : {n}")
print(f"Binary  : {n:b}")
print(f"Octal   : {n:o}")
print(f"Hex     : {n:x}")
print(f"HEX     : {n:X}")


print("\n" + "=" * 60)
print("10. Sign Formatting")
print("=" * 60)

positive = 12
negative = -12

print(f"{positive:+}")
print(f"{negative:+}")


print("\n" + "=" * 60)
print("11. Date Formatting")
print("=" * 60)

now = datetime.now()

print(f"Default : {now}")
print(f"Date    : {now:%Y-%m-%d}")
print(f"Time    : {now:%H:%M:%S}")
print(f"Full    : {now:%A, %B %d, %Y}")


print("\n" + "=" * 60)
print("12. Debug Syntax (Python 3.8+)")
print("=" * 60)

x = 15
y = 8

print(f"{x=}")
print(f"{y=}")
print(f"{x+y=}")


print("\n" + "=" * 60)
print("13. Conversion Flags")
print("=" * 60)

message = "Hello\nPython"

print(f"!s -> {message!s}")
print(f"!r -> {message!r}")
print(f"!a -> {message!a}")


print("\n" + "=" * 60)
print("14. Escaping Braces")
print("=" * 60)

print(f"{{This is inside braces}}")
print(f"2 + 3 = {2 + 3}")


print("\n" + "=" * 60)
print("15. Multiline f-Strings")
print("=" * 60)

first = "Alice"
last = "Johnson"

info = f"""
User Information
----------------
First Name : {first}
Last Name  : {last}
Full Name  : {first} {last}
"""

print(info)


print("=" * 60)
print("16. Practical Example")
print("=" * 60)

product = "Laptop"
price = 1299.99
tax = 0.085
quantity = 3

subtotal = price * quantity
total = subtotal * (1 + tax)

print(f"""
Receipt
-------
Product : {product}
Price   : ${price:.2f}
Qty     : {quantity}

Subtotal: ${subtotal:,.2f}
Tax     : {tax:.1%}
Total   : ${total:,.2f}
""")


print("=" * 60)
print("17. Everything Together")
print("=" * 60)

name = "Bob"
age = 32
salary = 78543.5

print(f"Employee: {name:<10} | " f"Age: {age:02} | " f"Salary: ${salary:,.2f}")
