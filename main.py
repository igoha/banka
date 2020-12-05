# uprava suborov z odvodmi a mzdami DSI CZ pre import do VUB
import sys


counter = 1
nazov_suboru = sys.argv[1]
file_ori = open(nazov_suboru)
file_new = open(nazov_suboru.replace(".cfd", "_new.cfd"), "w", encoding="utf-8")
for line in file_ori:
    if line.startswith("ZK:"):
        # na riadku ZK vymazat koncove medzery
        line = line.rstrip() + "\n"
    elif line.startswith("HD:"):
        # na riadku HD vymenit kod banky z 6800 na 6700
        # a vlozit poradove cislo polozky
        line = line.replace(" 6800 ", " 6700 ")
        line = line.replace(" 1 ", " " + str(counter) + " ")
        counter += 1
    file_new.write(line)
# na koniec suboru vlozit S3
file_new.write("S3:000000000 000")

file_ori.close()
file_new.close()
