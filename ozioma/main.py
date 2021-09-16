from ozioma import chat_bot_2, calculator
from ozioma.function_module import exercises

if __name__ == "__main__":
    print(exercises.max_of_three_numbers())
    print()
    print('Adding values within a list')
    print(exercises.add_values())
    print()
    print('Summing values within a list')
    print(exercises.sum_of_numbers_in_a_list())
    print()
    print('Multiplying values within a list')
    print(exercises.multiply_numbers_in_a_list())
    print()
    print('Reversing the order of a string')
    print(exercises.reverse_a_string())
    print()
    print('Finding the factorial of a number')
    print(exercises.factorial_of_a_number())
    print()
    print('Checking if a number is within an inputted range')
    print(exercises.check_number_within_a_range())
    print()
    print('Counting the number of upper and lower cases in a sentence')
    print(exercises.check_upper_and_lowercase_in_sentence())
    print()
    print('Creating a list of unique values from a list of values')
    print(exercises.create_a_list_with_unique_elements_of_given_list())
    print()
    print('Checking if a number is a prime number or not')
    print(exercises.find_prime_number())
    print()
    print('Printing the even numbers in a list')
    print(exercises.print_even_number_from_a_list())
    print('Thank you for partaking in our game.')

    # while True:
    #     input_number = input('Type 1 to chat, 2 to calculate two numbers or exit to exit the program: ')
    #     if input_number == '1':
    #         chat_bot_2.do_somthing()
    #     elif input_number == '2':
    #         calculator.calculate()
    #     elif input_number == 'exit':
    #         break