import sys
import re
from urllib.request import urlopen as url
# L'intervalle doit etre en premier argument
# Le port doit etre en seconde argument et il doit etre 8000

#on doit vérifier si les arguments ont été passés correctement
port = ""
if (len(sys.argv) > 2):
    if (re.match("[A-Z]-[A-Z]", sys.argv[1])
            and sys.argv[1][0] < sys.argv[1][2]):
        ## la focntion ord donne le code ascii d'un caractere
        Min = ord(sys.argv[1][0])
        Max = ord(sys.argv[1][2])
    else:
        print("erreur dans le premier argument\n")
    if (sys.argv[2] != "8000"):
        print("erreur : le port doit etre 8000\n")
    else:
        port = sys.argv[2]
else:
    # si l'intervalle des pages est inconnu on faire le traitement sur tous les pages
    if (len(sys.argv) == 2):
        port = "8000"
        print("le port n'a pas été spécifié , *** port = 8000")
        #si seulment l'intevalle ete specifie on doit le prendre en consideration
        if (re.match("[A-Z]-[A-Z]", sys.argv[1])
                and sys.argv[1][0] < sys.argv[1][2]):
            ## la focntion ord donne le code ascii d'un caractere
            Min = ord(sys.argv[1][0])
            Max = ord(sys.argv[1][2])
        else:
            print("erreur dans le premier argument\n")
    else:
        Min = ord("A")
        Max = ord("Z")

info = open("info.txt", 'w')
sum = 0
dic = open("subst.dic", 'w', encoding="utf-16-le")
for i in range(Min, Max + 1):
    #la fonction chr donne le caractere a partir d'un code ascii
    current_char = chr(i)

    link = url("http://127.0.0.1:" + port +
               "/vidal/vidal-Sommaires-Substances-" + current_char + ".htm")

    content = link.read().decode("utf-8")

    ##
    match = re.findall(r"(?<=[0-9]\.htm\">).+(?=</a>)", content)

    for j in match:
        dic.write(j + ",.N+subst\n")
    info.write("le nombre de med commencant par la lettre " + current_char +
               " est : " + str(len(match)) + "\n")
    sum = sum + len(match)
info.write("le nombre totale est " + str(sum))
info.close()