

def divide():
    x = int(input("What number is the numerator: "))
    while True:
        try:
            y = int(input("What number is the denominator: "))
            if y == 0:
                print("Division by zero is not allowed")
                continue
            return x/y
        except ValueError:
            print("Enter a number")

ans = divide()
print(ans)

  
