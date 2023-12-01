file = open('input.txt', 'r').readlines()
Q1_score, Q2_score = 0, 0

for line in file:
    Q1_digits, Q2_digits = [], []
    number_words = [
        'one', 'two', 'three',
        'four', 'five', 'six',
        'seven', 'eight', 'nine'
    ]

    # Check from each character in the line,
    for index, char in enumerate(line):
        # If it's a numerical digit, bang it in the list
        if char.isdigit():
            Q1_digits.append(char)
            Q2_digits.append(char)
            # and skip checking the rest of the string
            continue
    
        # Otherwise, look at the suffixing string, if there's a word, add digit
        for index_offset, word in enumerate(number_words):
            if line[index:].startswith(word):
                Q2_digits.append(str(index_offset + 1))

    Q1_line_value = int(Q1_digits[0] + Q1_digits[-1])
    Q2_line_value = int(Q2_digits[0] + Q2_digits[-1])

    Q1_score += Q1_line_value
    Q2_score += Q2_line_value

print(
    'Calibration value sum for Question 1:', Q1_score, 
    '\nCalibration value sum for Question 2:', Q2_score
)