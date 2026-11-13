# Poznámky pro správce skillu „rodokmen“

Sem Claude průběžně zapisuje, co by se mělo ve skillu zlepšit: chyby nástrojů, nové archivy a postupy, nápady.
Jen technické věci, žádné údaje o rodině. Nic se neposílá automaticky – když budete chtít, Claude poznámky vypíše
a vy je zkopírujete do e-mailu na sarsonj@gmail.com. Klidně připište i vlastní zkušenosti – užitečné změny autor rád
zapracuje do skillu, aby je měli i ostatní. Děkujeme!


- Cloud (claude.ai/code, prostředí Default s omezenou sítí): `novy_projekt.py --hlidac` zamítl bezpečnostní klasifikátor
  (zápis hooku do .claude/settings.json); bez `--hlidac` prošlo. `mista.py pridej` padá s tracebackem
  (URLError: Tunnel connection failed: 403) – chtělo by to srozumitelnou hlášku „OpenStreetMap není dostupná, povolte
  nominatim.openstreetmap.org“. Pro cloud by se hodila sekce v instalace.md: které hosty povolit a že MZA/ZA Opava
  (prohlížeč, CAPTCHA) v cloudu prakticky nejdou → doporučit práci na vlastním počítači.
- Skill jsem do cloudu instaloval kopií `skills/rodokmen` do `.claude/skills/rodokmen/` v repozitáři projektu
  (plugin v cloudovém kontejneru nepřežije); funguje, jen `verze.py`/aktualizace s tím možná nepočítá.
- MZA Acta Publica z cloudového kontejneru (headless Chromium/Playwright): stránka i `viewer` se načtou, ale dlaždice
  vrací HTTP 426 („Unable to open … HTTP 426 attempting to load TileSource“) – v cloudu MZA prakticky nejde.
  Hledání knih přes `slusne.py curl` funguje; parametr `page=2` vrátil stejné výsledky jako `page=1` (u obce s <20 knihami).
