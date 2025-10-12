#fonction pour la moyenne avec la gestion d'exception
def note ():
    ls_note =[]
    for i in range(4):
        try:
            note = float(input(f"Entrer la note: {i+1} en %: "))
            if note >= 0 or note <= 100:
                ls_note.append(note)
                print(ls_note)
            else:
                print("La note doit être comprise entre 0 et 100")
        except ValueError:
            print("Entrz un nomnbre valide")

    return ls_note

#fonction pour la moyenne somme diviser par la longueur
def note_len_sum (ls_note:list):
    return sum(ls_note)/len(ls_note)

def superieur_60(moyenne):
    return moyenne>60


if __name__ == '__main__':
    notes_examen = note()

    moyenne_avec_sum_len = note_len_sum(notes_examen)
    print(f"Moyenne (avec sum et len): {moyenne_avec_sum_len:.2f}%")

    resultat = superieur_60(moyenne_avec_sum_len)
    print(f"Est-ce que l'étudiant a une moyenne supérieure à 60 % ? {resultat}")