# Přímí předci podle Kekulého čísel: 1 = výchozí osoba (ten, pro koho rodokmen děláme),
# otec osoby n má číslo 2n, matka 2n+1. Tedy 2 = otec, 3 = matka, 4–7 prarodiče, 8–15 pradědečci a prababičky…
#
# Každá osoba:  číslo: dict(n="Jméno Příjmení", y="1850–1910", st="doc", f=[...], r=[...], note="...")
#   n    jméno; ženy rodným příjmením („Anna Dvořáková“), u nejistého čtení otazník („Marie Špalková (?)“)
#   y    roky života pro přehledy: "* 1931" (žije / úmrtí neznámé), "1850–1910", "asi 1720–1785", "1680 – před 1740"
#   st   stav doložení:  doc  = doloženo matrikou (čteno přímo ze snímku)
#                        prob = pravděpodobné (shoda údajů, ale ne přímý doklad)
#                        fam  = údaj od rodiny / z rodinného dokumentu
#                        mh   = jen z cizího rodokmenu na internetu (MyHeritage, Geni…) – neověřeno
#                        unk  = neznámé (jen místo v rodokmenu)
#   f    fakta jako krátké věty: "* 12. 3. 1873 Hořice čp. 477", "kovář", "× 28. 1. 1897 Anna Stejskalová", "† 14. 5. 1902"
#        (* narození, × sňatek, † úmrtí – podle těchto značek web pozná sňatky a místa pro mapu)
#   r    klíče zápisů z data/zaznamy.json, které osobu dokládají
#   note poznámka: proč je údaj nejistý, rozpory, odkud se vzal
#   sex  jen u osoby 1: "M" nebo "F" (u ostatních plyne z čísla)
# Žijící lidé: jen jméno a rok narození (soukromí), note="Žijící – údaje jen základní."
# Neznámý otec nemanželského dítěte: dict(n="otec neuveden", st="unk", f=[], note="…")

P = {
    1: dict(n="Petr Čerbák", y="* 1980", st="fam", sex="M", f=["* 1980 Ivančice"], r=[],
            note="Žijící – údaje jen základní."),
    2: dict(n="MUDr. Petr Čerbák", y="1948–2026", st="fam",
            f=["* 12. 1. 1948 Brno", "lékař", "† 3. 5. 2026 Brno", "pohřben v Ořechově u Brna"], r=[],
            note="Údaje od syna Petra."),
    3: dict(n="Hana Poláková", y="* 1955", st="fam", f=["* 1955 Brno", "zdravotní sestra"], r=[],
            note="Žijící – údaje jen základní."),
    4: dict(n="Cyrill Čerbák", y="1892–1965", st="fam",
            f=["* 1892", "pocházel z Kyjovic (okres Opava, u Ostravy)", "rodina bydlela také v Pusté Polomi", "† 1965"], r=[],
            note="Údaje od vnuka Petra. Byl o 18 let starší než manželka Miroslava – možná druhé manželství, ověřit."),
    5: dict(n="Miroslava Šnébergová", y="* 1910", st="fam", f=["* 1910 Říčany u Brna"], r=[],
            note="Údaje od vnuka Petra. Pravopis příjmení ověřit v matrice (Šnébergová / Schneeberg…)."),
    6: dict(n="Karel Polák", y="1923–1980", st="fam", f=["* 1923", "pocházel z Řicmanic", "† 1980"], r=[],
            note="Údaje od vnuka Petra."),
    7: dict(n="Eliška Pavlíková", y="1924–1990", st="fam", f=["* 1924", "pocházela z Tikovic", "† 1990"], r=[],
            note="Údaje od vnuka Petra. Tikovice jsou dnes část Ořechova u Brna."),
    9: dict(n="Annamarie Čerbáková", y="", st="fam", f=[], r=[],
            note="Matka dědy Cyrilla (od vnuka Petra). Rodné příjmení Čerbáková = stejné jako syn, Cyrill byl tedy "
                 "nejspíš nemanželský syn; ověřit v křestní matrice. Otec Cyrilla zatím neznámý."),
    14: dict(n="Tomáš Pavlík", y="", st="fam", f=[], r=[],
             note="Otec babičky Elišky (od vnuka Petra)."),
    15: dict(n="Anežka (rodné příjmení neznámé)", y="", st="fam", f=[], r=[],
             note="Matka babičky Elišky, provdaná Pavlíková (od vnuka Petra). Rodné příjmení zjistit v matrice."),
    18: dict(n="Josef Čerbák", y="", st="fam", f=[], r=[],
             note="Otec Annamarie Čerbákové (od vnuka Petra, potvrzeno)."),
    19: dict(n="Karolina (rodné příjmení neznámé)", y="", st="fam", f=[], r=[],
             note="Matka Annamarie, provdaná Čerbáková (od vnuka Petra). Rodné příjmení zjistit v matrice."),
}

# Rody = osm větví podle pradědečků a prababiček (čísla 8–15). Doplňte, jakmile je znáte:
# 8: ("Novákové", "Jedna věta, kdo to byli a odkud – ukáže se na webu u rodu."),
LINES = {
    9: ("Čerbákové", "Rod dědy Cyrilla z Kyjovic a Pusté Polomi u Ostravy – příjmení po matce Annamarii."),
    14: ("Pavlíkové", "Rod babičky Elišky z Tikovic u Ořechova."),
}

# Příbuzní mimo přímou linii (sourozenci, strýcové…): k = číslo předka, ke kterému patří.
# dict(k=16, n="Josef Novák (1865–1920)", t="Bratr Jana. Kovář v …", r=["klic_zapisu"])
SIDE = [
    dict(k=5, n="Cyrilla Šnebergová (* 1897)",
         t="Z Říčan č. 13, dcera rolníka Františka Šneberga a Františky roz. Mityškové(?). 4. 2. 1920 se v Říčanech "
           "provdala za Františka Koláře, rolníka z Ostrovačic. Možná starší sestra babičky Miroslavy – zatím neověřeno.",
         r=["ricany_oddani_frantisek_kolar_cyrilla_snebergova_1920"]),
]

# Rozpory a otevřené otázky (na web do „Co hledáme“) jako dvojice (otázka, odpověď). Odpověď začněte
# „Vyřešeno: …“ (na webu se skryje), „Hypotéza: …“ nebo „Otevřené: …“. Jde na web – nic citlivého.
# ("Kdy se narodil Jan Novák?", "Otevřené: rodina říká 1850, v Holicích 1848–1852 nenalezen.")
ISSUES = [
    ("Kdo byli rodiče babičky Miroslavy Šnébergové (* 1910 Říčany)?",
     "Hypotéza: v Říčanech č. 13 žil rolník František Šneberg s manželkou Františkou roz. Mityškovou(?); jejich dcera "
     "Cyrilla (* 1897) se vdala 1920. Miroslava mohla být její mladší sestra; Mityškovi se objevují i v rodinném vyprávění. "
     "Ověřit v rejstříku narozených Ostrovačice (kn. 1552)."),
]

# Hypotézy o původu rodu nad rámec doložené linie (zobrazí se na stránce rodu):
# dict(rod=8, nadpis="Hypotéza: Novákové z Lhoty", text="…", polozky=[("Jan Novák", "kmotr 1681…")], zaznamy=["klic"])
HYPOTEZY = [
]

# Předek v rodokmenu vícekrát (příbuzní rodiče): {alias: hlavní číslo}, např. {350: 140}
SAME = {}
