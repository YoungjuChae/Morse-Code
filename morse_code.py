# Author: Youngju Chae
# Morse Code with encryption and decryption

# Create necessary dictionary 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# Write code for encryption
def encrypt(message):
  # Create necessary variables
  message = message.upper()
  code = ''
  # Determine if character is a space or not
  for x in message:
    if x == ' ':
      code += '  '
    else:
      code += MORSE_CODE_DICT[x]
      code += ' '
  return code

# Write code for decryption
def decrypt(code):
  # Create necessary variables
  code += " "
  message = ''
  letter = ''
  # Determine if character is a space or not
  for c in code:
    if c != ' ':
      letter += c
      spaces = 0
    else:
      spaces += 1
      if spaces == 2:
        message += ' '
      else: 
        # Find correct value for each code
        key_list = list(MORSE_CODE_DICT.keys())
        value_list = list(MORSE_CODE_DICT.values())
        ind = value_list.index(letter)
        message += key_list[ind]
        letter = ""
  return message
      
# Determine user's choice
def morse_code():
  # Determine if user wants to encrypt or decrypt
  answer = input('Do you want to (e)ncrypt or (d)ecrypt a Morse Code? ')
  # Determine what message user wants to encrypt
  if answer  == 'e':
    message = input('Type your message: ')
    encryption = encrypt(message)
    print(encryption)
  # Determine what code user wants to decrpyt
  elif answer == 'd':
    code = input('Type your code: ')
    decryption = decrypt(code)
    print(decryption)
# Determine if user wants to continue
while(input("Do you want to use Morse Code? y or n: ") == 'y'):
  morse_code()
