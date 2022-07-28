import random; import string; import webbrowser

output = Element('output')

linkList = []

def generate(*args, **kwargs):
    # Main generate code
    letters, url_numbers = '', ''
    # Generate random letters
    for letter in range(2):
        letter = random.choice(string.ascii_letters)
        letters += letter
    # Generate random numbers
    for number in range(4):
        number = random.randint(0,9)
        number = str(number)
        url_numbers += number
    # Cat link together
    link = f'https://prnt.sc/{letters}{url_numbers}'.lower()
    # Append to list
    linkList.append(link)
    # Create string version of list to print
    stringList = ''
    for item in linkList: stringList += f'{item}, '
    # Display in HTML
    output.write(stringList)
    webbrowser.open_new_tab(link)
    # Add/remove classes for styling
    output.remove_class('has-text-grey-light')
    output.add_class('has-text-grey-darker')