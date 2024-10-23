"""
Write a program that takes an integer as input and return an integer with reversed digit
ordering.
For example: 
For input 500, the program should return 5. 
For input -56, the program should return -65. 
For input -90, the program should return -9. 
For input 91, the program should return 19.
"""

def reverse_digit(num):
    #If the number is negative, reverse the number and make it negative
    if num < 0:
        return -int(str(-num)[::-1])
    #If the number is positive, reverse the number
    else:
        return int(str(num)[::-1])

if __name__ == "__main__":
    #num = input("Enter an integer: ")
    num1 = 500
    print("Reversed integer:", reverse_digit(int(num1)))
    num2 = -56
    print("Reversed integer:", reverse_digit(int(num2)))
    num3 = -90
    print("Reversed integer:", reverse_digit(int(num3)))
    num4 = 91
    print("Reversed integer:", reverse_digit(int(num4)))