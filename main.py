import random


def main():
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    number3 = random.randint(0, 100)
    """
    ########################################
    Code Your Program here
    ########################################
    """
    print(number1,number2,number3)
    min_value= number1 
    min_value= number2 if number2<= min_value else min_value
    min_value= number3 if number3<= min_value else min_value
    print(min_value)
   
    ########################################
    # Do not delete the return statement
    ########################################
    return number1, number2, number3, min_value


if __name__ == '__main__':
    main()
