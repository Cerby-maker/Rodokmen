# Stav rodokmenu a pravidla práce

Tento soubor je vstupní bod. Po každém restartu (nová konverzace, zkrácený kontext) ho Claude čte jako první,
pak konec `research_log.md` a sekci „Rozpracováno“.

## Pro koho
- Výchozí osoba: Petr Čerbák, * 1980 Ivančice (u Brna)
- Kdo s Claudem pracuje a jak chce komunikovat: Petr sám; česky, stručně. Pracuje v cloudovém sezení (claude.ai) – localhost nevidí.

## Kde co je
| Soubor | Obsah |
|---|---|
| `data/osoby.py` | Přímí předci podle Kekulého čísla + rody, boční příbuzní, otevřené otázky, hypotézy. |
| `data/zaznamy.json` | Každý použitý zápis z matriky (klíč = název obrázku). |
| `data/svazky.json` | Matriční svazky (archiv, signatura, odkaz). |
| `data/prepisy.json` | Přepis originálu a český překlad každého zápisu. |
| `data/zvyrazneni.json` | Rámečky – které místo výřezu čteme. |
| `data/research_log.md` | Deník VŠECH hledání, i neúspěšných. |
| `data/udaje_od_rodiny.md` | Co řekla rodina, rodinné dokumenty. |
| `data/zajimavosti.md`, `data/pribeh.md` | Texty na web. |
| `data/archivni_dotazy.md` | Co by šlo zjistit jen v archivu. |
| `data/mista.json`, `data/dokumenty.json`, `data/web.json` | Mapa, rodinné fotky a dokumenty, nastavení webu. |
| `vyrezy/`, `zdroje/` | Výřezy zápisů pro web (1800 px) a v plném rozlišení. |
| `dokumenty/` | Rodinné dokumenty a fotky od uživatele (originály). |
| `pracovni/` | Pracovní soubory (stažené stránky, kontrolní obrázky) – nejdou na web. |
| `web/` | Rodinný web. `cd web && npm run nahled` (data + sestavení + náhled); po změně dat stačí `npm run data && npm run build`. |

## Pravidla
1. Než něco ohlásím jako nové, prohledám `osoby.py`, `zaznamy.json` a `research_log.md` (jméno, místo, rok).
2. Údaj je „doloženo“ (doc) jen tehdy, když jsem ho přečetl přímo na snímku. Čtení od pomocníků ověřím sám.
3. Každé hledání (i neúspěšné) zapíšu do `research_log.md`.
4. Nejistá čtení označím (?) – nic nedomýšlím.
5. Ke každému novému zápisu: výřez (`tools/vyrez.py`), rámeček (`tools/ramecek.py`) a přepis s překladem.
6. Po změně dat spustím `python3 -I tools/kontrola.py`.

## Rozpracováno (aktualizovat průběžně)
- Fáze 1 – rozhovor s rodinou: výchozí osoba, rodiče, 4 prarodiče, část pradědečků (9 Annamarie Čerbáková – Cyrill asi nemanželský; 14–15 Tomáš a Anežka Pavlíkovi; 18–19 Josef a Karolina Čerbákovi). Chybí: rodiče Miroslavy Šnébergové a Karla Poláka, sňatky, řemesla, dokumenty.
- Poznámka: Ivančice, Řicmanice, Tikovice, Říčany = MZA Brno (jen v prohlížeči); Kyjovice a Pustá Polom (okres Opava) = ZA Opava (soal_zoomify.py + prohlížeč).
- Síť: v cloudu (claude.ai) byly OpenStreetMap i archivy blokované → Petr pokračuje na svém počítači (Claude Code / desktop).
- Při prvním sezení na počítači: Fáze 0 dokončit – zkontrolovat Python/Node/ImageMagick/git, nabídnout hlídač sítě
  (`novy_projekt.py . --hlidac`, v cloudu ho nešlo zapnout), Playwright pro MZA a ZA Opava, a přidat místa na mapu
  (Brno, Ivančice, Ořechov, Tikovice, Řicmanice, Říčany u Brna, Kyjovice a Pustá Polom u Opavy).
- MZA v cloudu nejde (HTTP 426) → Petr posílá snímky obrazovky, já navádím na snímky a čtu. Funguje dobře.
- Nalezeno: sňatek Kolář × Cyrilla Šnebergová 1920 (Říčany č. 13, rodiče František Šneberg a Františka roz. Mityšková);
  Mityškovi jsou v rodinném vyprávění → silná stopa k rodičům babičky Miroslavy. Ověřit: index N Ostrovačice kn. 1552 (id 10031).
- Další krok v matrikách: děda Cyrill Čerbák * 1892 – křest v Kyjovicích (farnost? ZA Opava); Miroslava Šnébergová * 1910 Říčany (MZA).
- Kyjovice (ZA Opava, fara „Hr V“): knihy viz deník ř. 11. Cyrill * 1892 → N+I 1874–1907 (Hr V 11); Josef † 1898 → Z+I
  1865–1901 (Hr V 10); Jakub † 1766 → Z 1689–1795 (Hr V 4), sňatek → O 1690–1794 (Hr V 3); narození 1696 online není.
