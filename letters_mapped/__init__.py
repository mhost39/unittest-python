
digits = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
    '0': ' ',
}

# generate letter mapped like b = 22 and e = 33
letters_mapped = {} 
for k, v in digits.items():
    for i, c in enumerate(v):
        letters_mapped[c] = k * (i+1)

# function to convert letters to digits
def convert_letters_input(letters):
    M = letters.strip('\n') # remove newline spaces
    M = M.strip('\r')

    if len(M) < 1:
        return "not supported"
    for c in M:
        if ( (not c.isalpha()) and (not c == ' ') )  :
            return "not supported"
        if (c.isalpha() and c.isupper()):
            return "not supported"

    result = letters_mapped[M[0]]
    for c in M[1:]:
        k = letters_mapped[c]
        if k[0] == result[-1]:
            result += ' '
        result += k
  
    return result

# function to get key for value in dictionary
def get_key(val): 
    for key, value in letters_mapped.items(): 
         if val == value: 
             return key 
    return "not supported"

# function convert digits to letters  
def convert_digits_input(digits):
    digits = digits.strip('\n') # remove newline spaces 
    if len(digits) < 1:
        return "not supported"
    for c in digits:
        if not c.isdigit() and not c == ' ' :
            return "not supported"

    from itertools import groupby # to split string like 44555 is [44, 555]
    L = [''.join(g) for _, g in groupby(digits)]
    result = ''
    for i in L:
        if i == ' ':
            continue
        result += get_key(i)
    return result

def convert_letters():
    seed_file1_in = open("letters_mapped/seed-file1", "r")
    seed_file1_out = open("letters_mapped/seed-file1.out", "a")
    count = 1
    for t in seed_file1_in:
        result = convert_letters_input(t)
        seed_file1_out.write("Line #"+ str(count) +": " + result + '\n')
        count +=1
    seed_file1_in.close()
    seed_file1_out.close()

def convert_digits():
    seed_file2_in = open("letters_mapped/seed-file2", "r")
    seed_file2_out = open("letters_mapped/seed-file2.out", "a")
    count = 1
    for t in seed_file2_in:
        result = convert_digits_input(t[2:])
        seed_file2_out.write("Line #"+ str(count) +": " + result + '\n')
        count +=1
    seed_file2_in.close()
    seed_file2_out.close()
