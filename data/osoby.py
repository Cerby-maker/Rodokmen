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
            note="Údaje od vnuka Petra. Byl o 18 let starší než manželka Miroslava – možná druhé manželství, ověřit. "
                 "Strom na MyHeritage (neověřeno) uvádí * 12. 5. 1892, † 28. 1. 1965."),
    5: dict(n="Miroslava Šnebergová", y="* 1910", st="doc", f=["* 2. 7. 1910 Říčany", "dcera Františka Šneberga"],
            r=["ostrovacice_index_n_miroslava_snebergova_1910"],
            note="Rejstřík narozených Ostrovačice (kn. 1552, sn. 64): „1910 … 2/7 Šnebergová Miroslava, dcera Františka, "
                 "Říčany, str. 509“. Sama kniha narozených online není. Rodina píše „Šnébergová“, matrika „Šnebergová“."),
    6: dict(n="Karel Polák", y="1923–1980", st="fam", f=["* 1923", "pocházel z Řicmanic", "† 1980"], r=[],
            note="Údaje od vnuka Petra."),
    7: dict(n="Eliška Pavlíková", y="1924–1990", st="fam", f=["* 1924", "pocházela z Tikovic", "† 1990"], r=[],
            note="Údaje od vnuka Petra. Tikovice jsou dnes část Ořechova u Brna."),
    9: dict(n="Annamarie Čerbáková", y="asi 1874–1880 – ?", st="fam", f=[], r=[],
            note="Matka dědy Cyrilla (od vnuka Petra). Rodné příjmení Čerbáková = stejné jako syn, Cyrill byl tedy "
                 "nejspíš nemanželský syn; ověřit v křestní matrice. Otec Cyrilla zatím neznámý. "
                 "MyHeritage (neověřeno): narozena mezi 1874 a 1880."),
    10: dict(n="František Šneberg", y="* 1868", st="prob",
             f=["* 29. 3. 1868 Říčany", "rolník v Říčanech č. 13", "× 26. 5. 1896 Říčany Františka Mityšková"],
             r=["ricany_oddani_frantisek_sneberg_frantiska_mityskova_1896", "ostrovacice_index_n_miroslava_snebergova_1910",
                "ricany_oddani_frantisek_kolar_cyrilla_snebergova_1920"],
             note="Sňatek 1896 doložen. Že je otcem Miroslavy, plyne z rejstříku („dcera Františka“, Říčany) – jiný "
                  "František Šneberg v Říčanech zatím není znám; křestní zápis Miroslavy online není."),
    11: dict(n="Františka Mityšková", y="* 1869", st="prob",
             f=["* 8. 3. 1869 Říčany č. 3", "× 26. 5. 1896 Říčany František Šneberg"],
             r=["ricany_oddani_frantisek_sneberg_frantiska_mityskova_1896",
                "ricany_oddani_frantisek_kolar_cyrilla_snebergova_1920"],
             note="Sňatek 1896 doložen; matka Cyrilly (sňatek 1920). Že je i matkou Miroslavy, je pravděpodobné "
                  "(rejstřík uvádí jen otce). Mityškovi se objevují v rodinném vyprávění."),
    14: dict(n="Tomáš Pavlík", y="", st="fam", f=[], r=[],
             note="Otec babičky Elišky (od vnuka Petra)."),
    15: dict(n="Anežka (rodné příjmení neznámé)", y="", st="fam", f=[], r=[],
             note="Matka babičky Elišky, provdaná Pavlíková (od vnuka Petra). Rodné příjmení zjistit v matrice."),
    20: dict(n="Václav Šneberg", y="", st="doc", f=["čtvrtláník v Říčanech", "žil ještě 1896"],
             r=["ricany_oddani_frantisek_sneberg_frantiska_mityskova_1896", "ricany_oddani_josef_mitysek_juliana_snebergova_1896"],
             note="Otec Františka a Juliány Šnebergových (sňatky 1896). Svědek obou sňatků „Václav Šneberg, domkář "
                  "z Říčan“ může být on, nebo jiný Václav (otec je v zápisu čtvrtláník, svědek domkář)."),
    21: dict(n="Kateřina Šupková", y="", st="doc", f=[],
             r=["ricany_oddani_frantisek_sneberg_frantiska_mityskova_1896", "ricany_oddani_josef_mitysek_juliana_snebergova_1896"],
             note="Matka Františka a Juliány Šnebergových (sňatky 1896: „Kateřiny roz. Šupka“)."),
    22: dict(n="Ignác Mityšek", y="", st="doc", f=["čtvrtláník v Říčanech č. 3"],
             r=["ricany_oddani_frantisek_sneberg_frantiska_mityskova_1896", "ricany_oddani_josef_mitysek_juliana_snebergova_1896",
                "ricany_oddani_frantisek_kolar_cyrilla_snebergova_1920"],
             note="Otec Františky a Josefa Mityškových (sňatky 1896). Zda v roce 1896 žil, čtu nejistě („živ.“)."),
    23: dict(n="Marie Konečná", y="", st="doc", f=["žila v Říčanech, ještě 1896"],
             r=["ricany_oddani_frantisek_sneberg_frantiska_mityskova_1896", "ricany_oddani_josef_mitysek_juliana_snebergova_1896"],
             note="Matka Františky a Josefa Mityškových (sňatky 1896: „Marie roz. Konečný“). Svědek Jan Konečný, "
                  "čtvrtláník z Říčan, byl nejspíš její příbuzný."),
    18: dict(n="Josef Čerbák", y="1829–1898", st="doc",
             f=["* 8. 3. 1829 Kyjovice", "× 18. 5. 1858 Kyjovice Karolína Vaňková",
                "× 5. 2. 1883 Kyjovice Anastasia Vavrečková", "chalupník v Kyjovicích č. 42",
                "† 22. 8. 1898 Kyjovice č. 42 (69 let, sešlost věkem), pohřben 24. 8."],
             r=["kyjovice_umrti_josef_cerbak_1898"],
             note="Úmrtí doloženo matrikou (Kyjovice č. 42, syn Jana Čerbáka a Nepomuceny roz. Illíkové). Otec Annamarie "
                  "(od vnuka Petra). Narození, sňatky a druhá manželka Anastasia Vavrečková (* 27. 2. 1852) ze stromu "
                  "na MyHeritage – zatím neověřeno."),
    19: dict(n="Karolína Vaňková", y="1837–1882", st="mh", f=["* 1837", "× 18. 5. 1858 Kyjovice Josef Čerbák", "† 25. 6. 1882"], r=[],
             note="Matka Annamarie (od vnuka Petra). Rodné příjmení a data jen ze stromu na MyHeritage – neověřeno."),
    36: dict(n="Jan Čerbák", y="1801–1867", st="doc", f=["* 15. 1. 1801 Kyjovice č. 16", "chalupník v Kyjovicích", "† 1867"],
             r=["kyjovice_umrti_josef_cerbak_1898"],
             note="Jméno a povolání (chalupník v Kyjovicích) doloženo zápisem o úmrtí syna Josefa 1898. Data narození "
                  "a úmrtí ze stromu na MyHeritage; rejstřík zemřelých Kyjovice má „Čerbak Johann“ na str. 4 (asi 1867)."),
    37: dict(n="Johanna Nepomucena Illíková", y="1805–1869", st="doc", f=["* 22. 8. 1805", "† 1869"],
             r=["kyjovice_umrti_josef_cerbak_1898"],
             note="Jméno a původ (dcera kováře Jakoba Illíka) doloženo zápisem o úmrtí syna Josefa 1898. Data ze stromu "
                  "na MyHeritage; rejstřík zemřelých Kyjovice má „Čerbak Nepomucena“ na str. 7 (asi 1869)."),
    38: dict(n="Ondřej Vaněk", y="", st="mh", f=[], r=[],
             note="Otec Karolíny – jen ze stromu na MyHeritage, neověřeno."),
    39: dict(n="Mechtilda Kubíčková", y="", st="mh", f=[], r=[],
             note="Matka Karolíny – jen ze stromu na MyHeritage, neověřeno."),
    72: dict(n="Joseph Čerbák", y="", st="mh", f=[], r=[],
             note="Otec Jana – jen ze stromu na MyHeritage, neověřeno."),
    73: dict(n="Magdalena Havrlantová", y="", st="mh", f=[], r=[],
             note="Matka Jana – jen ze stromu na MyHeritage („Magdalena Havrlant“), neověřeno."),
    144: dict(n="Šimon Čerbák", y="1745–1806", st="mh", f=["* 1745", "† 1806"], r=[],
              note="Otec Josepha – jen ze stromu na MyHeritage, neověřeno."),
    145: dict(n="Anna Vavrečková", y="? – 1817", st="mh", f=["† 1817"], r=[],
              note="Matka Josepha – jen ze stromu na MyHeritage („Anna Vavrečka“), neověřeno."),
    288: dict(n="Jakub Čerbák", y="asi 1696–1766", st="prob", f=["* asi 1696", "švec v Kyjovicích", "† 2. 12. 1766 (?) Kyjovice, pohřben v Pusté Polomi"],
              r=["pusta_polom_umrti_jakub_cerbak_1766"],
              note="Úmrtí doloženo matrikou: „Jacobus Czerbak, sutor, Kiowitio, 70 annorum“ (rok zatím z MyHeritage). "
                   "Že je otcem Šimona (* 1745), uvádí jen strom na MyHeritage – mezičlánky Joseph a Šimon zatím neověřeny."),
    289: dict(n="Rosina Nováková", y="", st="mh", f=[], r=[],
              note="Matka Šimona podle stromu na MyHeritage – ten u ní uvádí narození 1765, což nejde (syn Šimon * 1745). "
                   "Buď je rok chybně, nebo jde o jinou ženu (druhá manželka Jakuba?). Neověřeno."),
    74: dict(n="Jakub Illík", y="", st="doc", f=["kovář v Kyjovicích"], r=["kyjovice_umrti_josef_cerbak_1898"],
             note="Otec Johanny Nepomuceny – doloženo zápisem o úmrtí vnuka Josefa 1898 („Jakoba Illíka, kováře v Kyjovicích“)."),
    75: dict(n="Terezie Bubeníková", y="", st="mh", f=[], r=[],
             note="Matka Johanny – jen ze stromu na MyHeritage („Theresia Bubeníková“), neověřeno."),
}

# Rody = osm větví podle pradědečků a prababiček (čísla 8–15). Doplňte, jakmile je znáte:
# 8: ("Novákové", "Jedna věta, kdo to byli a odkud – ukáže se na webu u rodu."),
LINES = {
    10: ("Šnebergové", "Rod babičky Miroslavy, rolníci v Říčanech u Brna (č. 13)."),
    11: ("Mityškovi", "Rod prababičky Františky z Říčan u Brna – známý i z rodinného vyprávění."),
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
    dict(k=2, n="Roman Čerbák (* 1932)",
         t="Starší bratr tatínka Petra, syn Cyrilla a Miroslavy, narozený 1932 v Ostravě (podle rodiny).", r=[]),
    dict(k=18, n="Sourozenci Annamarie: Františka, Emma, František, Otilie, Ferdinand",
         t="Děti Josefa Čerbáka a Karolíny Vaňkové podle stromu na MyHeritage (neověřeno).", r=[]),
    dict(k=18, n="Nevlastní sourozenci Annamarie: Rudolf, Josef, Jan, Arnošta",
         t="Děti Josefa Čerbáka z druhého manželství s Anastasií Vavrečkovou (* 1852, sňatek 1883) podle stromu "
           "na MyHeritage (neověřeno).", r=[]),
    dict(k=36, n="Sestry Josefa: Anna, Františka", t="Podle stromu na MyHeritage (neověřeno).", r=[]),
    dict(k=10, n="Juliána Šnebergová (* 1862)",
         t="Sestra Františka. 26. 5. 1896 – týž den jako on – se v Říčanech vdala za Josefa Mityška, bratra jeho nevěsty "
           "Františky: dvojí svatba dvou sourozeneckých párů.",
         r=["ricany_oddani_josef_mitysek_juliana_snebergova_1896"]),
    dict(k=11, n="Josef Mityšek (* 1866)",
         t="Bratr Františky, rolník v Říčanech č. 3. 26. 5. 1896 se oženil s Juliánou Šnebergovou, sestrou Františkova "
           "ženicha. V roce 1920 byl svědkem na svatbě své neteře Cyrilly („Josef Mityšek, rolník v Říčanech č. 3“).",
         r=["ricany_oddani_josef_mitysek_juliana_snebergova_1896", "ricany_oddani_frantisek_kolar_cyrilla_snebergova_1920"]),
]

# Rozpory a otevřené otázky (na web do „Co hledáme“) jako dvojice (otázka, odpověď). Odpověď začněte
# „Vyřešeno: …“ (na webu se skryje), „Hypotéza: …“ nebo „Otevřené: …“. Jde na web – nic citlivého.
# ("Kdy se narodil Jan Novák?", "Otevřené: rodina říká 1850, v Holicích 1848–1852 nenalezen.")
ISSUES = [
    ("Kdo byli rodiče babičky Miroslavy Šnébergové (* 1910 Říčany)?",
     "Hypotéza (zesílená): rejstřík narozených uvádí „Miroslava, dcera Františka“. V Říčanech č. 13 žil rolník František Šneberg s manželkou Františkou roz. Mityškovou(?); jejich dcera "
     "Cyrilla (* 1897) se vdala 1920. Miroslava mohla být její mladší sestra; Mityškovi se objevují i v rodinném vyprávění. "
     "Ověřit v rejstříku narozených Ostrovačice (kn. 1552)."),
    ("Kdo byla matka Šimona Čerbáka (* 1745)?",
     "Otevřené: strom na MyHeritage uvádí Rosinu Novákovou * 1765 – o 20 let mladší než její údajný syn. Chyba ve stromu; "
     "ověřit v matrikách."),
    ("Kdy se narodila Juliána Šnebergová, sestra Františka?",
     "Vyřešeno: na ostřejším snímku je 29. 11. 1862 (věk 34), ne 1868 – rozpor s bratrem Františkem (* 1868) zmizel."),
]

# Hypotézy o původu rodu nad rámec doložené linie (zobrazí se na stránce rodu):
# dict(rod=8, nadpis="Hypotéza: Novákové z Lhoty", text="…", polozky=[("Jan Novák", "kmotr 1681…")], zaznamy=["klic"])
HYPOTEZY = [
]

# Předek v rodokmenu vícekrát (příbuzní rodiče): {alias: hlavní číslo}, např. {350: 140}
SAME = {}
