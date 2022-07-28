import random; import string; import webbrowser

output = Element('output')

def generate(*args, **kwargs):
    letters, url_numbers = '', ''
    for letter in range(2):
        letter = random.choice(string.ascii_letters)
        letters += letter
    for number in range(4):
        number = random.randint(0,9)
        number = str(number)
        url_numbers += number
    link = f'https://prnt.sc/{letters}{url_numbers}'.lower()
    output.write(link)
    webbrowser.open_new_tab(link)