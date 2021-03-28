import random
import os

# a list of every possible character that can be chosen to represent the language 
possiblechar = ['А', 'Б', 'В', 'Г', 'Д', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 
'Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω', 'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'ς', 'σ', 'τ', 'υ', 'φ', 
'₡', '₢', '₣', '₤', '₥', '₦', '₧', '₨', '₩', '₪', '₫', '€', '₭', '₮', '₯', '₰', '₱', '₲', '₳', '₴', '₵', '₶', '₷', '₸', '₹', '₺', '₻', '₼', '₽', '₾', '₿', 'ɐ', 
'ɑ', 'ɒ', 'ɓ', 'ɔ', 'ɕ', 'ɖ', 'ɗ', 'ɘ', 'ə', 'ɚ', 'ɛ', 'ɜ', 'ɝ', 'ɞ', 'ɟ', 'ɠ', 'ɡ', 'ɢ', 'ɣ', 'ɤ', 'ɥ', 'ɦ', 'ɧ', 'ɨ', 'ɩ', 'ɪ', 'ɫ', 'ɬ', 'ɭ', 'ɮ', 'ɯ', 'ɰ', 'ɱ', 'ɲ', 'ɳ', 'ɴ', 'ɵ', 'ɶ', 'ɷ', 'ɸ', 'ɹ', 'ɺ', 'ɻ', 'ɼ', 'ɽ', 'ɾ', 'ɿ', 'ʀ', 'ʁ', 'ʂ', 'ʃ', 'ʄ', 'ʅ', 'ʆ', 'ʇ', 'ʈ', 'ʉ', 'ʊ', 'ʋ', 'ʌ', 'ʍ', 'ʎ', 'ʏ', 'ʐ', 'ʑ', 'ʒ', 'ʓ', 'ʔ', 'ʕ', 'ʖ', 'ʗ', 'ʘ', 'ʙ', 'ʚ', 'ʛ', 'ʜ', 'ʝ', 'ʞ', 'ʟ', 'ʠ', 'ʡ', 'ʢ', 'ʣ', 'ʤ', 'ʥ', 'ʦ', 'ʧ', 'ʨ']

# a dictionary of all randomally generated words in the language
lexicon = {"language":"ჰ", "ash":"Æ"}
script = ''

# a function to create symbols for words and remove them from the list of possible characters that can be chosen
def define(word):
    lexicon[word] = possiblechar[random.randint(0, len(possiblechar)-1)]
    possiblechar.remove(lexicon[word])


#defines words in the language
wordlist = ['me', 'hello', 'what', 'person', 'be','you', 'place', 'no', 'yes', 'good']
for word in wordlist:
    define(word)

# creates a list of the characters in a random order to be copied and pasted
for word in lexicon:
    script += lexicon[word]
l = list(script)
random.shuffle(l)
script = ''.join(l)

# prints the list of characters
def printscript():
    print(script)

# function to wipe the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear') 
    printscript()

# a function to respond to inputs given by the player
def respond(*words):
    sentence = ''
    for i in words:
        sentence += i + ' ' 
    response = input('\n' + sentence + '\n')
    analyse(response)

# a function to analyse what the player has said and response appropriately
def analyse(response):
    if response == 'exit':
            quit
    elif response == lexicon['person'] + ' ' + lexicon['what'] + ' ' + lexicon['be'] + ' ' + lexicon['you'] + ' ?':
        respond(lexicon['me'], lexicon['be'], lexicon['ash'])
    elif response == lexicon['me'] + ' ' + lexicon['be'] + ' ' + lexicon['ash']:
        respond(lexicon['no'], '.', lexicon['me'], lexicon['be'], lexicon['ash'])
    elif response == lexicon['you'] + ' ' + lexicon['be'] + ' ' + lexicon['ash']:
        respond(lexicon['yes'], '.', lexicon['me'], lexicon['be'], lexicon['ash'])
    elif response == lexicon['no'] + ' . ' + lexicon['me'] + ' ' + lexicon['be'] + ' ' + lexicon['ash']:
        respond(lexicon['no'], '.', lexicon['me'], lexicon['be'], lexicon['ash'])
    elif response == lexicon['me'] + ' ?':
        respond(lexicon['you'] + ' ^')
    elif response == lexicon['ash'] + ' ?':
        respond(lexicon['ash'], lexicon['be'], lexicon['me'])
    elif response == lexicon['person']:
        respond(lexicon['person'], lexicon['what'], '?')
    elif response == lexicon['person'] + ' ?':
        respond(lexicon['me'], lexicon['be'], lexicon['person'], '.', lexicon['you'], lexicon['be'], lexicon['person'])
    elif response == lexicon['be']:
        respond(lexicon['what'], lexicon['be'], lexicon['what'], '?')
    else:
        respond(lexicon['what'], '?')

# the mainfunction of the game, starts the game and proceeds to the main loop
if __name__ == '__main__': 
    printscript()
    respond(lexicon['person'], lexicon['what'], lexicon['be'], lexicon['you'], '?')
