#this functions removes all the unwnated symbols from user input
def trim(inp_str):
    #all the unwanted symbols
    ignored_symbols = (' ','@','#','$','%','^','&','*','(',')','_','+','=','[',']','{','}',\
    ':',';','<','>','/','\\','|','~','.',',','\'','"','!','?','-')
    new_str = ""
    #we check the string by symbol
    for symb in inp_str:
        #and if the symbol isn't an unwanted, we add it to a new "trimmed" string
        #otherwise we ignore it
        if symb not in ignored_symbols:
            new_str += symb
    return new_str.casefold()

#this function reverses the user input
def reverse(inp_str):
    return inp_str[::-1]

#this function checks if the user input is a palindrome
def is_palindrome(inp_str):
    #if the string equals to the reversed string
    #than it's a palindrome
    if trim(inp_str) == reverse(trim(inp_str)):
        return "\nYep!"
    else:
        return "\nNope..."

#this function checks if user entered "quit"
def is_quit(inp_str):
    if trim(inp_str) == "quit":
        return True
    else:
        return False
        
print("\nLet's check, if a phrase is a palindrome.")
#while loop to keep the program running
while True:
    #user inputs some text
    user_text = input("\nEnter something. Enter \"quit\" to quit (we all know it's not a palindrome: ")
    #we check if he entered "quit" and stop the program in that case
    if is_quit(user_text):
        break
    #otherwise we check and tell the user, if user input is a palindrome
    print("\n" + is_palindrome(user_text))