# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
Project_01_Examinator_app.py

* Vytvořte terminálovou aplikaci, která bude čerpat otázky ze souborů z definovaného adresáře.
* Aplikace zatím nebude využívat OOP, resp. třídy a instance.
* Aplikaci vložíte jméno a příjmení zkoušeného.
* Aplikaci lze zadat počet otázek, které budou součástí aktuálního testu.
* Apliace náhodně vybere otázky, zamíchá jejich odpovědi, zobrazí postupně jednu po druhé, vždy smaže terminál, ať netřeba scrollovat.
* Aplikace vyhodnotí jednotlivé otázky.
* Na výstupu bude také počet správně a špatně zodpovězených otázek, procentní úspěšnost.
* Známka dle procentního rozdělení: <100-90>,(90-75>,(75-60>,(60-45>,(45-0>
* Možnost v kódu nastavit konstanty pro procentní rozdělení a jiné známkování - na jednom místě.
* Výsledek se vždy uloží do podadresáře "Vysledky_testu" ve tvaru: "prijmeni_jmeno_20241006_132845_pocetOtazek_znamka.txt"
* Formát souboru viz níže. 
* Možnost celý test zopakovat s nově vybranými otázkami ze souborů.
* U každé otázky bude vždy zobrazen autor a název souboru, ze kterého jsme čerpali.
* Aplikace hlídá vstupy od uživatele, množství otázek ze souboru a množství otázek v testu.


## SOUBOR S VÝSLEDKEM TESTU - definice
    Výsledek se vždy uloží do podadresáře "Vysledky_testu" 
    Pojmenování souboru bude ve tvaru: "prijmeni_jmeno_20241006_132845_pocetOtazek_znamka.txt"
    Uvnitř souboru bude vždy stejná struktura a vyhodnocení jednoho pokusu jednoho testu:


## SOUBOR S VÝSLEDKEM TESTU - ukázkový soubor "valek_vladislav_20241006_132845_10_2.txt"
        Vypracoval/a: Vladislav Válek
        Otázek v testu: 10
        Výsledná známka: 2
        Procentní úspěšnost: 80 %
        Stupnice: <100-90>,(90-75>,(75-60>,(60-45>,(45-0>
        Datum a čas vyhodnocení: 6.10.2024, 13:25:45

        ----------------------
        Chybně zodpovězeno:

        Otázka: Která z následujících možností představuje správnou syntaxi pro definici funkce v Pythonu? 
        definice funkce my_function(): 
        function my_function() {} 
        def my_function(): 
        fun my_function():

        Otázka: Který z následujících příkazů vytvoří řetězec v Pythonu? 
        'Hello, World!' 
        Hello, World! 
        12345 
        ["Hello", "World"]
        ----------------------


## SOUBOR S OTÁZKAMI - definice
Vždy musíte dodržet PŘESNĚ následující strukturu:
    Na prvním řádku je vždy uveden autor otázek.
    Každá otázka má před sebou 2x prázdný řádek.
    Otázka začíná slovem "Otázka:" a zadáním této otázky.
    Každá odpověď začíná nulou nebo jedničkou se středníkem a mezerou.
    Počet odpovědí je vždy 4, přitom je právě jedna z nich správná.
    Odpovědi ani otázky nejsou číslovány ani označeny písmeny - lze je tedy volně zamíchat, včetně míchání odpovědí.
    Název souboru s otázkami bude pojmenován dle vzoru: "valek_vladislav_otazky_libovolne_pojmenovani.txt"
    Bude uložen v podadresáři "Testy_zdroj_otazek"
Počet otázek v souboru bude minimálně 20. Lze jakkoliv využít cokoliv, každý autor ručí za správnost, nespoléhat se na ...


## SOUBOR S OTÁZKAMI - ukázkový soubor "valek_vladislav_otazky_albatros.txt"
        Autor: Vladislav Válek


        Otázka: Jakým způsobem se v Pythonu odliší blok řádků kódu, který patří k jedné funkci?
        0; Blok je uzavřen do trojitých uvozovek.
        0; Každý řádek začíná otazníkem.
        1; Všechny řádky jsou odsazeny ideálně o 4 mezery.
        0; Celý blok je uzavřen do složených závorek.


        Otázka: Která z následujících možností představuje správnou syntaxi pro definici funkce v Pythonu? 
        0; definice funkce my_function(): 
        0; function my_function() {} 
        1; def my_function(): 
        0; fun my_function():


        Otázka: Jakým způsobem definujeme seznam v Pythonu? 
        1; Použitím hranatých závorek: [1, 2, 3] 
        0; Použitím kulatých závorek: (1, 2, 3) 
        0; Použitím složených závorek: {1, 2, 3} 
        0; Pomocí příkazu create list
"""


import os
import random
import time
from datetime import datetime


##############################################################
# Globální konstanty a proměnné

GRADE_THRESHOLDS




##############################################################
def load_questions_from_directory(directory):
    """Načtení všech otázek z textových souborů v zadaném adresáři.
    Args:
        directory: str, cesta k adresáři s otázkami.
    Returns:
        list, seznam všech otázek načtených ze souborů.
    """


##############################################################
def parse_questions(content, author, filename):
    """Parses the content of a file with questions into a list of dictionaries.
    Args:
        content: str, obsah souboru s otázkami.
        author: str, jméno autora otázek.
        filename: str, název souboru.
    Returns:
        list, seznam otázek ve formě slovníku.
    """


##############################################################
def shuffle_answers(question):
    """Zamíchá odpovědi u zadané otázky.
    Args:
        question: dict, jedna otázka se správnou odpovědí.
    Returns:
        dict, otázka se zamíchanými odpověďmi.
    """


##############################################################
def get_user_name():
    """Získá jméno a příjmení zadané uživatelem."""


##############################################################
def get_number_of_questions(total_questions):
    """Získá od uživatele počet otázek, které chce mít v testu.
    Args:
        total_questions: int, maximální počet dostupných otázek.
    Returns:
        int, počet otázek pro test.
    """


##############################################################
def ask_question(question, index):
    """Zobrazí otázku a odpovědi uživateli, získá jeho odpověď.
    Args:
        question: dict, otázka se zamíchanými odpověďmi.
        index: int, pořadí otázky.
    Returns:
        bool, True pokud uživatel odpověděl správně, jinak False.
    """


##############################################################
def calculate_grade(score, total_questions):
    """Vypočítá výslednou známku podle procentní úspěšnosti.
    Args:
        score: int, počet správných odpovědí.
        total_questions: int, celkový počet otázek v testu.
    Returns:
        int, výsledná známka.
    """


##############################################################
def save_test_result(first_name, last_name, total_questions, score, grade, success_rate, wrong_answers):
    """Uloží výsledek testu do souboru v zadaném formátu.
    Args:
        first_name: str, jméno uživatele.
        last_name: str, příjmení uživatele.
        total_questions: int, celkový počet otázek.
        score: int, počet správných odpovědí.
        grade: int, výsledná známka.
        success_rate: float, procentní úspěšnost.
        wrong_answers: list, seznam nesprávně zodpovězených otázek.
    """


##############################################################
def run_test():
    """Hlavní funkce, která řídí průběh testu."""


##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":

    os.system('clear' if os.name == 'posix' else 'cls')

    while True:
        run_test()
        repeat = input("Chcete test zopakovat? (a/n): ").lower()
        if repeat != "a":
            break
