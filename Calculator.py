while True:
    expression = input("Enter expression (or '='to exit) and numbers: ")
    if expression == "=":
        break
    try:
        answer = eval(expression)
        print("Answer =", answer)
    except ZeroDivisionError:
        print("Error:cannot divide by zero.")
    except:
        print("invalid expression")