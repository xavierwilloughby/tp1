#xavier willoughby

#number of words count_words
def count_word(chaine):
        words = chaine.split()
        nbr_of_words = len(words)
        return nbr_of_words


# ask for the sentence
chaine = input("donne une phrase: \n")
#define the number of words
nbr_of_words = count_word(chaine)

#retourne le nombre de mots dans la chaine
print("Le nombre de mots est : \n", nbr_of_words)