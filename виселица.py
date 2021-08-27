def check_mistake(w, q):
    for i in w:
        if i == q:
            return False
    return True
def check_win(t):
    for i in t:
        if i == "_":
            return True
    return False
def get_word(w):
    return w[0]
def start_template (w):
    t = []
    for i in w:
        t.append("_")
    return t
def welcomte_speech(t):
    print(f"загаданое слово состоит из {len(t)} букв")
def list_to_string_convert(t):
    s = ""
    return s.join(t)
def user_input():
    return input("введите букву: ")
def build_tepmlate (t, w, g=""):
    a = 0
    for i in w:
        if i == g:
            t[a] = g
        a = a + 1
    return t
def game():
    progress = True
    word = ["banana"]
    lifes = 3
    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcomte_speech(list_to_string_convert(template))
    while progress:
        user_quess = user_input()
        template = build_tepmlate(template, word_in_play, user_quess)
        last_list = list_to_string_convert(template)
        print(last_list)
        progress = check_win(last_list)
        if check_mistake(word_in_play, user_quess):
            lifes = lifes - 1
        if lifes == 0:
            print("жизни закончились, вы проиграли:(")
            break
        if progress == False:
            print("вы отгадали слово!")
            break
game()
