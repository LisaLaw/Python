#transforming text to and from leet speak

user_input = input('Enter your string: ') #asking the user for a string input, can be either leet or not

my_str = user_input.upper() #transforms the string into all upper case letters
my_output = []

#defines function to translate each letter in the string
def transform(letter, list1) :
    #assign leet speak to normal letters
    if letter == 'A': 
        new_letter = '4'
    elif letter == 'B':
        new_letter = '6'
    elif letter == 'E':
        new_letter = '3'
    elif letter == 'I':
        new_letter = '|'
    elif letter == 'L':
        new_letter = '1'
    elif letter == 'M':
        new_letter = '(V)'
    elif letter == 'N':
        new_letter = '(\)'
    elif letter == 'O':
        new_letter = '0'
    elif letter == 'S':
        new_letter = '5'
    elif letter == 'T':
        new_letter = '7'
    elif letter == 'V':
        new_letter = '\/'
    elif letter == 'W':
        new_letter = '`//'
    #assign normal letters to leet speak
    elif letter == '4':
        new_letter = 'A'
    elif letter == '6':
        new_letter = 'B'
    elif letter == '3':
        new_letter = 'E'
    elif letter == '|':
        new_letter = 'I'
    elif letter == '1':
        new_letter = 'L'
    elif letter == '{':
        new_letter = 'M'
    elif letter == '}':
        new_letter = 'N'
    elif letter == '0':
        new_letter = 'O'
    elif letter == '5':
        new_letter = 'S'
    elif letter == '7':
        new_letter = 'T'
    elif letter == '*':
        new_letter = 'V'
    elif letter == '%':
        new_letter = 'W'  
    #unaffected letters 
    else: new_letter = letter
    #put all letters back together to a string
    list1.append(new_letter)

#function to store all leet letters into single characters
def single_charas(string1) :
    if r'(V)' in string1:
        string1 = string1.replace(r'(V)', '{')
    if r'(\)' in string1:
        string1 = string1.replace(r'(\)', '}')
    if r'\/' in string1:
        string1 = string1.replace(r'\/', '*')
    if r'`//' in string1:
        string1 = string1.replace(r'`//', '%')
    return string1

#call on function to turn all letters into single characters, if needed
new_str = single_charas(my_str)

#translates each letter in the user input via transform function
for letter in new_str:
    transform(letter, my_output) #input each letter of string into function as parameter 1 and empty list as parameter 2

print('')
print('The translation to/from leetspeak is: ', ''.join(my_output)) #print output as a list