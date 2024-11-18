"""1.1 Feladat
Készíts egy programot, amely a felhasználó által megadott mondatról a mondatvégi jel alapján eldönti milyen fajtájú!
 (kijelentő, kérdő, felkiáltó / felszólító / óhatjtó)"""

megadott_mondat = input("Kérlek adj meg egy mondatot: ")

if megadott_mondat[-1] == ".":
    print(" EZ a mondat kijelento. ")
elif megadott_mondat.endswith("?"):
    print("Ez a mondat kérdő.")
elif megadott_mondat[-1] == "!":
    print("Ez a mondat felkialto / ohajto. ")
else:
    print("Nem adtál meg mondat vegi irasjelet. ")

#endswith tema