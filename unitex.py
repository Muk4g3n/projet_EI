import os

os.system("rd /s 80jours_snt")
os.mkdir("80jours_snt")
os.system("UnitexToolLogger Normalize 80jours.txt -r norm.txt")
os.system("UnitexToolLogger Tokenize 80jours.snt -a Alphabet.txt")
os.system("UnitexToolLogger Dico -t 80jours.snt -a Alphabet.txt Dela_fr.bin")
os.system("UnitexToolLogger Grf2Fst date.grf")
os.system("UnitexToolLogger Grf2Fst date.grf")
os.system(
    "UnitexToolLogger Locate -t 80jours.snt date.fst2 -a Alphabet.txt -L -I --all"
)
os.system(
    "UnitexToolLogger Concord -t 80jours_snt/concord.int -f \"courrier new \" -s 12 -l 40 -r 55"
)
