def calculator():
    print("Simple calculator")
    print("Addition(+)")
    print("Subtraction(-)")
    print("Multiplication(*)")
    print("Division(/)")
    operation=input("Enter the operation to be performed on two numbers(+/-/*//):")
    if operation not in ('+','-','*','/'):
        print("Enter a valid choice to perform the operation")
        return
    try:
        num1=int(input("Enter number1:"))
        num2=int(input("Enter number2:"))
    except ValueError:
        print("Invalid choice of numbers")
        return
    if operation=='+':
        result=num1+num2
        print("The sum of numbers {num1} and {num2} is {result}")
    elif operation=='-':
        result=num1-num2
        print("The difference of numbers {num1} and {num2} is {result}")
    elif operation=='*':
        result=num1*num2
        print("Result when the numbers {num1} and {num2} are multiplied is {result]")
    else:
        if num2==0:
            print("Division by zero is not possible")
        else:
            result=num1/num2
            print("Result when the numbers {num1} and {num2} are divided is {result}")
#function call or run the function
calculator()
    
