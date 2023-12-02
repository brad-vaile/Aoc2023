import time

entries = []

string_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def is_potential_number_string(input):
    for s_number in string_numbers:
        if input in s_number:
            return True
    return False

def is_exact_number_string(input):
    for s_number in string_numbers:
        if input == s_number:
            return string_numbers.index(s_number)+1
    return 0
def load_file():
    with open(r'') as input_file:
        for line in input_file:
            entries.append(line.replace("\n", ""))

def find_number_digit(input : str, reverse : bool):
    number_string = ''
    for character in input:
        if(character.isnumeric()):
            return character
        else:

            if(reverse):
                number_string = character + number_string
            else:
                number_string += character

            if(is_potential_number_string(number_string)):
                ## is it an exact number in string form
                number = is_exact_number_string(number_string)
                if(number != 0):
                    return str(number)
            else:
                if(reverse):
                    number_string = number_string[:-1]
                else:
                    number_string = number_string[1:]
    return ''


if __name__ == '__main__':
    start = time.time()
    load_file()
    inputNumbers = []
    for entry in entries:
        num = find_number_digit(entry, False) + find_number_digit(entry[::-1], True)
        inputNumbers.append(int(num))

    print(sum(inputNumbers))
    end = time.time()
    print(f"Time taken to run the code was {end - start} seconds")


