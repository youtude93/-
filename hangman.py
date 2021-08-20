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
def game():
    progress = True
    word = ["orange"]
    lifes = 3
    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcomte_speech(list_to_string_convert(template))
    while progress:
        user_quess = user_input()