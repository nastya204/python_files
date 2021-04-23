def game():
    progress = True
    word = ["orange"]
    lifes = 3
    word_in_play = get_word(word)
    templane = srart_template(word_in_play)
    welcome_speech(list_to_string_convert(template))
    while progress:
        user_guess = user_input()
def user_input():
    """
    output: return str, built-in input() function
    """
    return input("Введите букву: ")
    
def welcome_speech(t):
    print(f'''
    Добро пожаловать в игру - hangman 2000
    Ваща задача угадать загаданное слово за несколько попыток,
    иначе вас ждет расплата!
    Загаданное слово состоит из {len(t)} букв {t}
    ''')

def start_template(w):
    """
    input: w - string(word)
    output: replace all chars in string to "_"
        return replaced chars as string with length w==t
    """
    t = []
    for l in w:
        t.append("_")
    return t

def list_to_string_convert(t):
    s = ""
    return s.join(t)

def get_word(w):
    """
    input: w- list eith string (words)
    output: for now: first element in list as string
    """
    return w[0]


