def get_book_text(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content

def get_num_words(text):
    return len(text.split())

def character_occurence_in_text(text):
    words = text.split() # on recupère chaque mot du texte
    my_dic = {}

    for word in words: # on parcoure chaque mot recuperé
        for letter in word: # on parcour chaque lettre dans le mot
            letter = letter.lower()
            if letter in my_dic: # si le mot est dans le dictionnaire, on fait +1
                my_dic[letter] += 1
            else: # sinon on ajoute dans le dictionnaire
                my_dic[letter] = 1

    return my_dic

def sort_on(item): # fonction utilitaire pour le tri
    return item['count']

def reorganize_dict(a_dict = {"a": 12, "b": 2}):
    a_list = [] # on crée une liste vide
    for key in a_dict: # on parcour les clés du dictionnaire
        if key.isalpha():
            a_list.append({"char": key, "count": a_dict[key]}) # on ajoute au tableau le nouveau dict

    a_list.sort(reverse=True, key=sort_on) # on tri le tableau 
    return a_list # on retourne la liste triée