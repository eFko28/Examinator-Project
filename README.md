# Základní soubory pro práci v semináři

První set pro elementární znalosti a jejich zdokonalení.

## 1. Soubory v Pythonu

Mrkni na *.py soubory. Zde by VŽDY měl být postup – nejdříve **EMPTY soubory** se zadáním a nápovědou. Základem jsou jednohvězdičkové úkoly, o které se máte pokoušet nejprve sami (90 % času). Potom s nápovědou z internetu + AI, ale nesklouzávejte k rychlému ústupu a snadné cestě. Bohužel se časem ukáže, že tohle bude spíše na škodu. Na to je vždy dost času i později, teď jde o zažití samotného **programování**, přemýšlení, hledání chyb ve vlastním kódu, vytrvání u kódování, když to zrovna nejde hladce.

---

## 2. Dokumentace kódu

Ne příliš oblíbená část, někdy přímo prudérní. Přesto na ni trvám a chci, ať ji děláte již od samotných začátků. Má to být **zvyk**, ne hrozba od šéfa. Dodržujte nastavené standardy.

Nejčastější pocit programátora je, že ten kód je tak jasný a průzračný, že není co dokumentovat, komentovat. V tom se musí vyznat i **deb..** Schválně se zeptejte všech, co již programují ve větších firmách a v týmech.

Ten pocit zná každý, většina už ale přišla i do styku s kódem, který nebyl popsaný (protože je to přeci jasné) a ve kterém se měli vyznat a zorientovat. Samozřejmě se vám to nakonec povede, ale mohlo to být daleko snazší, kdyby byl kód veden a popisován předem. 

---

## 3. Komentáře v kódu

Kromě docstrings rozhodně doporučuji následující - když přidáváte do kódu podmínky, protože něco nefungovalo, je velmi vhodné napsat základní info, proč tohle a tohle přidáváte. Co se tím ošetří a které případy to zachytí. Samozřejmě, když už to píšete, tak je to přeci průzračně jasné a netřeba to ještě komentovat. **Uvidíte.**

Nepodlehněte klamu, kdy znáte svůj kód v okamžiku, kdy jej tvoříte.

---

## 4. Čtení kódu s řešením

Předposledním krokem by mělo být čtení kódu v souboru *.py s řešením. Hned na začátku tvrdím, že rozhodně si nekladu za cíl vytvořit dokonalý kód. Dokonce věřím a doufám, že váš kód bude lepší a čitelnější. Snad nasáváte všechny impulsy jako houba a získáváte cvik, na který já už nemám dost času ani procvičování.

V řešení se naučte číst, dívejte se, co je řešeno jinak, rozšiřte svůj kód, pokud uznáte, že něco z toho je šikovné, že něco jste opomněli, že něco je navíc. Kupodivu i tato část je velmi důležitá, protože budete propojovat svůj kód s někým dalším, provádíte vlastně merge a učíte se hledat, proč to nefunguje vám, ale "jemu" jo.

---

## 5. Úkoly s více hvězdičkami

Úkoly s více hvězdičkami jsou něco jako rozšíření, pokud budete mít chuť a sílu, hledejte řešení sami. Pokud ne, rozhodně stále pro vás platí prostudování kódu v řešení. Někde budou části kódu zakomentované, někde je třeba něco zkusit nebo změnit.

Stále se učíte číst kód. **Cizí kód.** To bude tak 40 % vašeho "programování". Nevěšte hlavu, pokud narazíte na partie, které ještě nemáte "probrány", tak to normálně chodí. Mrkněte na zdroják poprvé, příště zase někde uvidíte podobný kód, časem to bude snazší a snazší, i když dané knihovny nebo obraty ještě neznáte. Netřeba luštit každý detail, něco se časem utřepe samo.


# GitHub Workflow

## *Co potřebuji?*

- **Vscode**
- **Git**

    &emsp;  Jak zjistím, jestli mám git nainstalovaný? Do příkazového řádku *vlož* příkaz:

    &emsp;  *`git --version`*

    &emsp;  Pokud se vyhodí ${\color{red}{error}}$ znamená to, že git **není nainstalovaný**.

## *Jak stáhnout materiály z githubu? Repozitář Shared:*

- **Otevři vscode** a **otevři si složku**, kde chceš soubory z githubu **stáhnout** stisknutím *`Ctrl + K Ctrl + O`*.

- Stiskni *`Ctrl + J`* k **otevření terminálu** a **vlož** příkaz:

    *`git clone https://vladislavvalek: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@github.com/vladislavvalek/Prg24-26-shared_01.git`*

- Vytvoří se složka a pak si jí zase můžete otevřít jako v prvním kroku.

## *A to mám pokaždé toto dělat, když se něco v repositáři změní?*

${\color{red}NE}$, pokud máte **otevřený ve vscode** repositář, dají se změny **stáhnout** jednoduchým příkazem:

&emsp;&emsp; *`git pull`*

## *Examinator - projekt - repozitář:*

*`git clone https://vladislavvalek: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@github.com/vladislavvalek/Prg24-26_Project_01_Examinator_app.git`*
