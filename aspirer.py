import sys
import re
from urllib.request import urlopen as url

if (len(sys.argv) > 2):
    if (re.match("[A-Z]-[A-Z]", sys.argv[1])
            and sys.argv[1][0] < sys.argv[1][2]):
        Min = ord(sys.argv[1][0])
        Max = ord(sys.argv[1][2])
    else:
        print("erreur dans le premier argument")
else:
    Min = ord("A")
    Max = ord("Z")
info = open("info.txt", 'a')
sum = 0
dic = open("subst.dic", 'a', encoding="utf-16-le")
for i in range(Min, Max + 1):
    current_char = chr(i)
    link = url("http://127.0.0.1/vidal/vidal-Sommaires-Substances-" +
               current_char + ".htm")
    content = link.read().decode("utf-8")
    # print(content)
    match = re.findall(r"(?<=[0-9]\.htm\">).+(?=</a>)", content)
    for j in match:
        dic.write(j + ",.N+subst\n")
    info.write("le nombre de med commencant par la lettre " + current_char +
               " est : " + str(len(match)) + "\n")
    sum = sum + len(match)
info.write("le nombre totale est " + str(sum))
info.close()