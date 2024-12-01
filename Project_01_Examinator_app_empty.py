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


# Globální konstanty a proměnné

GRADE_THRESHOLDS = {
    1: (90, 100),
    2: (75, 90),
    3: (60, 75),
    4: (45, 60),
    5: (0, 45)
}

QUESTIONS_FOLDER = "Testy_zdroj_otazek"

RESULTS_FOLDER = "Vysledky_testu"


def load_questions_from_directory(directory):
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


def parse_questions(content, author, filename):
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


def shuffle_questions(question):
    answers = question["answers"]
    correct_answer = question["correct_answer"]

    indices = list(range(len(answers)))
    random.shuffle(indices)

    new_correct_answer_index = new_answers.index(correct_answer)

    new_answers = [answers[i] for i in indices]
    new_correct_answer = new_answers[new_correct_answer_index]

    question["answers"] = new_answers
    question["correct_answer"] = new_correct_answer
    return question


def get_user_name():
    first_name = input("Zadejte své jméno: ")
    last_name = input("Zadejte své příjmení: ")

    return first_name, last_name


def get_number_of_questions(max_questions):
    number_of_questions = input(f"S kolika otázkami si přejete pracovat? max({max_questions})")
    return number_of_questions


def ask_question(question, index):
    os.system("cls")

    print(f"Autor: {question["author"]}, Zdroj: {question["file"]}")
    print(f"\nOtázka: {question["question"]}")
    
    for i, answer in enumerate(question["answer"]):
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

def calculate_grade(score, max_questions):
    percentage = (score / max_questions) * 100

    
    for grade, (lower, upper) in GRADE_THRESHOLDS.items():
        if lower <= percentage < upper:
            return grade
        
def save_test_result(first_name, last_name, total_questions, percentage, grade, success_rate, wrong_answers):
    

    time = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename_result = f"{last_name}_{first_name}_{time}_{total_questions}_{grade}.txt"
    filepath = os.path.join(RESULTS_FOLDER, filename_result)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(f"Vypracoval/a: {first_name} {last_name}")
        file.write(f"Otázek v testu: {total_questions}")
        file.write(f"Výsledná známka: {grade}")
        file.write(f"Procentní úspěšnost: {percentage}")
        file.write(f"Stupnice: {GRADE_THRESHOLDS}")
        file.write(f"Datum a čas vyhodnocení: {datetime.now().strftime("%d.%m.%Y, %H:%M:%S")}\n")

    if wrong_answers != "":
            file.write("\n----------------------\nChybně zodpovězeno:\n")
            for question in wrong_answers:
                file.write(f"\nOtázka: {question['question']}\n")
                for answer in question['answers']:
                    file.write(f"{answer}\n")

def run_examinator():
    first_name, last_name = get_user_name()

    questions = load_questions_from_directory(QUESTIONS_FOLDER)

    number_of_questions = get_number_of_questions(len(questions))

    selected_questions = random.sample(questions, number_of_questions)
    for question in selected_questions:
        shuffle_questions(question)

    score = 0
    wrong_answers = []

    
    for i, question in enumerate(selected_questions):
        if ask_question(question, i):
            score += 1
        else:
            wrong_answers.append(question)
    
    
    grade, percentage = calculate_grade(score, number_of_questions)
    

    
    print("\nTest dokončen!")
    print(f"Správně: {score}/{number_of_questions}")
    print(f"Procentní úspěšnost: {round(percentage, 2)}%")
    print(f"Výsledná známka: {grade}")

    
    save_test_result(first_name, last_name, number_of_questions, score, grade, percentage, wrong_answers)


##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":

    os.system('clear' if os.name == 'posix' else 'cls')
    while True:
        run_examinator()
        repeat = input("Chcete test zopakovat? (Y/n): ").lower()
        if repeat != "y":
            break

        