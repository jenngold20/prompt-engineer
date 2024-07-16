#I need random code that make a function for sum between 2 numbers
import random   
def sum_between_2_numbers(n1, n2):
    return random.randint(n1, n2) + random.randint(n1, n2)

def main():
    print(sum_between_2_numbers(10, 20))
    print(sum_between_2_numbers(100, 200))
    print(sum_between_2_numbers(1000, 2000))
    print(sum_between_2_numbers(10000, 20000))
    
    