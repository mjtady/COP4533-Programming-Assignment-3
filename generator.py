import random
from src.hvlcs import HighestValueCommonSubsequence

def generate_test_data(filename, stringLength):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    k = len(alphabet)

    # generate random character values for a-z
    charValues = {char: random.randint(1, 10) for char in alphabet}

    # generate two random strings of specified length
    strA = ''.join(random.choice(alphabet) for _ in range(stringLength))
    strB = ''.join(random.choice(alphabet) for _ in range(stringLength))

    # write the test data to  file
    with open(filename, 'w') as file:
        file.write(f"{k}\n")
        for char, value in charValues.items():
            file.write(f"{char} {value}\n")
        file.write(strA + '\n')
        file.write(strB + '\n')

def generate_test_data_output(in_filename, out_filename):
    with open(in_filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()] 
        k = int(lines[0])
        charValues = {}

        for i in range(1, k + 1):
            pair = lines[i].split()
            if len(pair) == 2:
                charValues[pair[0]] = int(pair[1])

        strA = lines[k + 1]
        strB = lines[k + 2]
        value, subsequence = HighestValueCommonSubsequence.maximumValue(strA, strB, charValues)

    with open(out_filename, 'w') as file:
        file.write(f"{value}\n")
        file.write(f"{subsequence}\n")

if __name__ == "__main__":
    # generate test data
    generate_test_data('data/test.in', 8)
    # generate expected output for the test data
    generate_test_data_output('data/test.in', 'data/test.out')