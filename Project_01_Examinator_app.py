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


        Otázka: Jak lze v Pythonu získat délku seznamu my_list? 
        1; Použitím funkce len(my_list) 
        0; Použitím funkce size(my_list) 
        0; Použitím metody my_list.length() 
        0; Pomocí příkazu list_size(my_list)


        Otázka: Co vrátí následující příkaz: print(3 == 3)? 
        0; True, protože Python vrací vždy ve funkci print hodnotu True. 
        1; True, protože porovnání čísel je v Pythonu korektní a rovná se. 
        0; False, protože dvojité rovnítko není správný porovnávací operátor. 
        0; SyntaxError, protože je potřeba použít === pro porovnání.


        Otázka: Co se stane při pokusu o změnu prvku v n-tici (tuple)? Například my_tuple[0] = 10. 
        0; Prvek v n-tici bude změněn na novou hodnotu. 
        0; Python přepíše n-tici bez chybové hlášky. 
        0; Python automaticky vytvoří kopii n-tice. 
        1; Python vyvolá chybu, protože n-tice jsou neměnné (immutable).


        Otázka: Jakým způsobem lze importovat modul math a použít funkci sqrt pro výpočet druhé odmocniny v Pythonu? 
        1; import math; math.sqrt(16) 
        0; from sqrt import math(); sqrt(16) 
        0; import sqrt.math from math; sqrt(16) 
        0; include math.sqrt(16)


        Otázka: Který z následujících příkazů vytvoří řetězec v Pythonu? 
        1; 'Hello, World!' 
        0; Hello, World! 
        0; 12345 
        0; ["Hello", "World"]


        Otázka: Co se stane při použití příkazu my_list.append(10)? 
        0; Do seznamu bude vloženo číslo 10 na první pozici. 
        1; Do seznamu bude přidán prvek 10 na jeho konec. 
        0; Seznam bude zkopírován a číslo 10 bude přidáno do nové kopie. 
        0; Python vyvolá chybu, protože pro přidání prvku je potřeba použít add().

"""


import os
import random
import time
from datetime import datetime



##############################################################
# Globální konstanty a proměnné

GRADE_THRESHOLDS = {        # Konfigurace známkování (procentní hranice)
    1: (90, 100),
    2: (75, 90),
    3: (60, 75),
    4: (45, 60),
    5: (0, 45)
}

QUESTIONS_FOLDER = "Testy_zdroj_otazek"
RESULTS_FOLDER = "Vysledky_testu"

os.chdir(os.path.dirname(os.path.abspath(__file__)))    #nastavení pracovního adresáře na akt. soubor

##############################################################
def load_questions_from_directory(directory):
    """Načtení všech otázek z textových souborů v zadaném adresáři.
    Args:
        directory: str, cesta k adresáři s otázkami.
    Returns:
        list, seznam všech otázek načtených ze souborů.
    """
    questions = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                author = file.readline().strip()
                content = file.read().strip()
                questions_in_file = parse_questions(content, author, filename)
                questions.extend(questions_in_file)
    return questions


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
    questions = []
    blocks = content.split("\n\n\n")
    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) >= 5 and lines[0].startswith("Otázka:"):
            question = {
                'question': lines[0].replace("Otázka:", "").strip(),
                'answers': [line[3:].strip() for line in lines[1:5]],
                'correct_answer': next(i for i, line in enumerate(lines[1:5]) if line.startswith("1;")),
                'author': author,
                'file': filename
            }
            questions.append(question)
    return questions


##############################################################
def shuffle_answers(question):
    """Zamíchá odpovědi u zadané otázky.
    Args:
        question: dict, jedna otázka se správnou odpovědí.
    Returns:
        dict, otázka se zamíchanými odpověďmi.
    """
    answers = question['answers']
    correct_answer = question['correct_answer']
    indices = list(range(len(answers)))
    random.shuffle(indices)
    shuffled_answers = [answers[i] for i in indices]
    new_correct_answer = indices.index(correct_answer)
    question['answers'] = shuffled_answers
    question['correct_answer'] = new_correct_answer
    return question


##############################################################
def get_user_name():
    """Získá jméno a příjmení zadané uživatelem."""
    last_name = input("Zadejte své příjmení: ")
    first_name = input("Zadejte své jméno: ")
    return first_name, last_name


##############################################################
def get_number_of_questions(total_questions):
    """Získá od uživatele počet otázek, které chce mít v testu.
    Args:
        total_questions: int, maximální počet dostupných otázek.
    Returns:
        int, počet otázek pro test.
    """
    while True:
        try:
            num_questions = int(input(f"Zadejte počet otázek (max {total_questions}): "))
            if 1 <= num_questions <= total_questions:
                return num_questions
            else:
                print(f"Zadejte číslo v rozsahu 1 až {total_questions}.")
        except ValueError:
            print("Prosím zadejte platné číslo.")


##############################################################
def ask_question(question, index):
    """Zobrazí otázku a odpovědi uživateli, získá jeho odpověď.
    Args:
        question: dict, otázka se zamíchanými odpověďmi.
        index: int, pořadí otázky.
    Returns:
        bool, True pokud uživatel odpověděl správně, jinak False.
    """
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # Přidán výpis autora a souboru otázek
    print(f"{question['author']} (zdroj: {question['file']})")
    
    print(f"Otázka {index + 1}: {question['question']}\n")
    for i, answer in enumerate(question['answers']):
        print(f"{i + 1}. {answer}")
    
    while True:
        try:
            user_answer = int(input("Zadejte číslo správné odpovědi: ")) - 1
            if 0 <= user_answer < len(question['answers']):
                return user_answer == question['correct_answer']
            else:
                print(f"Zadejte číslo v rozsahu 1 až {len(question['answers'])}.")
        except ValueError:
            print("Prosím zadejte platné číslo.")


##############################################################
def calculate_grade(score, total_questions):
    """Vypočítá výslednou známku podle procentní úspěšnosti.
    Args:
        score: int, počet správných odpovědí.
        total_questions: int, celkový počet otázek v testu.
    Returns:
        int, výsledná známka.
    """
    success_rate = (score / total_questions) * 100
    for grade, (min_percent, max_percent) in GRADE_THRESHOLDS.items():
        if min_percent <= success_rate <= max_percent:
            return grade, success_rate
    return 5, success_rate


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
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    result_filename = f"{last_name}_{first_name}_{timestamp}_{total_questions}_{grade}.txt"
    os.makedirs(RESULTS_FOLDER, exist_ok=True)
    filepath = os.path.join(RESULTS_FOLDER, result_filename)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(f"Vypracoval/a: {first_name} {last_name}\n")
        file.write(f"Otázek v testu: {total_questions}\n")
        file.write(f"Výsledná známka: {grade}\n")
        file.write(f"Procentní úspěšnost: {success_rate:.2f} %\n")
        file.write(f"Stupnice: {GRADE_THRESHOLDS}\n")
        file.write(f"Datum a čas vyhodnocení: {datetime.now().strftime('%d.%m.%Y, %H:%M:%S')}\n")
        if wrong_answers:
            file.write("\n----------------------\nChybně zodpovězeno:\n")
            for question in wrong_answers:
                file.write(f"\nOtázka: {question['question']}\n")
                for answer in question['answers']:
                    file.write(f"{answer}\n")


##############################################################
def run_test():
    """Hlavní funkce, která řídí průběh testu."""
    # Načtení otázek z adresáře
    questions = load_questions_from_directory(QUESTIONS_FOLDER)
    
    # Získání jména a počtu otázek
    first_name, last_name = get_user_name()
    num_questions = get_number_of_questions(len(questions))

    # Výběr náhodných otázek a zamíchání jejich odpovědí
    selected_questions = random.sample(questions, num_questions)
    selected_questions = [shuffle_answers(q) for q in selected_questions]

    score = 0
    wrong_answers = []

    # Zobrazení otázek a zaznamenání odpovědí
    for i, question in enumerate(selected_questions):
        if ask_question(question, i):
            score += 1
        else:
            wrong_answers.append(question)
    
    # Výpočet známky a úspěšnosti
    grade, success_rate = calculate_grade(score, num_questions)

    # Výpis výsledků
    print("\nTest dokončen!")
    print(f"Správně: {score}/{num_questions}")
    print(f"Procentní úspěšnost: {success_rate:.2f}%")
    print(f"Výsledná známka: {grade}")

    # Uložení výsledků
    save_test_result(first_name, last_name, num_questions, score, grade, success_rate, wrong_answers)


##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":

    os.system('clear' if os.name == 'posix' else 'cls')

    while True:
        run_test()
        repeat = input("Chcete test zopakovat? (ano/ne): ").lower()
        if repeat != "ano":
            break
