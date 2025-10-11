text = input("Enter a word: ")

# 2) Gérer le cas vide
if not text:
    print("")  # rien à afficher
else:
    # 3) Commencer le résultat avec le 1er caractère
    result = text[0]

    # 4) Parcourir du 2e caractère jusqu'au dernier
    for i in range(1, len(text)):
        # 5) Ajouter si différent du précédent
        if text[i] != text[i - 1]:
            result += text[i]

    # 6) Afficher le résultat final
    print(result)