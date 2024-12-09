import os
import random
import time
from datetime import datetime

GRADE_THRESHOLDS = {1: (90, 100), 2: (75, 90), 3: (60, 75), 4: (45, 60), 5: (0, 45)}
QUESTIONS_FOLDER = "Testy_zdroj_otazek"
RESULTS_FOLDER = "Vysledky_testu"


def load_questions_from_directory(directory):
    """
    Loads all questions from text files in the specified directory.

    Each file is expected to contain an author line, followed by the questions.

    Args:
        directory (str): Path to the directory containing question files.

    Returns:
        list: A list of questions parsed from the files.
    """
    questions = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                author = file.readline().replace("Autor: ", "").strip()
                content = file.read().strip()
                questions_in_file = parse_questions(content, author, filename)
                questions.extend(questions_in_file)
    return questions


def parse_questions(content, author, filename):
    """
    Parses the content of a file into individual questions.

    Args:
        content (str): The text content of the file.
        author (str): Author of the questions.
        filename (str): Name of the file the questions were sourced from.

    Returns:
        list: A list of question dictionaries with metadata.
    """
    questions = []
    blocks = content.split("\n\n\n")
    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) >= 5 and lines[0].startswith("Otázka:"):
            question = {
                "question": lines[0].replace("Otázka:", "").strip(),
                "answers": [line[3:].strip() for line in lines[1:5]],
                "correct_answer": next(i for i, line in enumerate(lines[1:5]) if line.startswith("1;")),
                "author": author,
                "file": filename,
            }
            questions.append(question)
    return questions


def get_user_name():
    """
    Prompts the user to enter their first and last name.

    Returns:
        tuple: A tuple containing the first name and last name as strings.
    """
    first_name = input("Zadejte své jméno: ")
    last_name = input("Zadejte své příjmení: ")

    return first_name, last_name


def get_number_of_questions(max_questions):
    """
    Prompts the user to select the number of questions for the test.

    Ensures the number is within the valid range.

    Args:
        max_questions (int): The maximum number of questions available.

    Returns:
        int: The number of questions chosen by the user.
    """
    while True:
        try:
            number_of_questions = int(input(f"S kolika otázkami si přejete pracovat? max({max_questions}): "))
            if 1 <= number_of_questions <= max_questions:
                return number_of_questions
            else:
                print(f"Zadejte číslo v rozsahu 1 až {max_questions}.")
        except ValueError:
            print("Prosím zadejte platné číslo.")


def ask_question(question, index):
    """
    Presents a question to the user and checks their answer.

    Args:
        question (dict): The question dictionary containing text, answers, and metadata.
        index (int): The index of the current question.

    Returns:
        bool: True if the user's answer is correct, False otherwise.
    """
    os.system("cls")

    print(f"Autor: {question['author']}, Zdroj: {question['file']}")
    print(f"\nOtázka: {question['question']}")

    for i, answer in enumerate(question["answers"]):
        print(f"{i + 1}. {answer}")

    while True:
        try:
            user_answer = int(input("Zadejte číslo správné odpovědi: ")) - 1
            if 0 <= user_answer < len(question["answers"]):
                return user_answer == question["correct_answer"]
            else:
                print(f"Zadejte číslo v rozsahu 1 až {len(question['answers'])}.")
        except ValueError:
            print("Prosím zadejte platné číslo.")


def calculate_grade(score, total_questions):
    """
    Calculates the grade based on the user's score.

    Args:
        score (int): The number of correctly answered questions.
        total_questions (int): The total number of questions.

    Returns:
        tuple: A tuple containing the grade (int) and percentage (float).
    """
    percentage = (score / total_questions) * 100
    for grade, (min_percent, max_percent) in GRADE_THRESHOLDS.items():
        if min_percent <= percentage <= max_percent:
            return grade, percentage
    return 5, percentage


def save_test_result(first_name, last_name, total_questions, percentage, grade, wrong_answers):
    """
    Saves the user's test results to a file.

    Args:
        first_name (str): User's first name.
        last_name (str): User's last name.
        total_questions (int): Total number of questions in the test.
        percentage (float): User's percentage score.
        grade (int): Final grade.
        wrong_answers (list): List of incorrectly answered questions.

    Returns:
        None
    """
    time = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename_result = f"{last_name}_{first_name}_{time}_{total_questions}_{grade}.txt"
    filepath = os.path.join(RESULTS_FOLDER, filename_result)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(f"Vypracoval/a: {first_name} {last_name}\n")
        file.write(f"Otázek v testu: {total_questions}\n")
        file.write(f"Výsledná známka: {grade}\n")
        file.write(f"Procentní úspěšnost: {percentage:.2f}%\n")
        file.write(f"Stupnice: {GRADE_THRESHOLDS}\n")
        file.write(f"Datum a čas vyhodnocení: {datetime.now().strftime('%d.%m.%Y, %H:%M:%S')}\n")

        if wrong_answers:
            file.write("\n----------------------\nChybně zodpovězeno:\n")
            for question in wrong_answers:
                file.write(f"\nOtázka: {question['question']}\n")
                for answer in question["answers"]:
                    file.write(f"{answer}\n")


def run_examinator():
    """
    Runs the main exam logic, including user interaction, question presentation, and result saving.

    Returns:
        None
    """
    first_name, last_name = get_user_name()

    questions = load_questions_from_directory(QUESTIONS_FOLDER)
    number_of_questions = get_number_of_questions(len(questions))

    selected_questions = random.sample(questions, number_of_questions)

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

    save_test_result(first_name, last_name, number_of_questions, percentage, grade, wrong_answers)


##############################################################
### Spuštění programu - MAIN
if __name__ == "__main__":
    os.system("clear" if os.name == "posix" else "cls")
    while True:
        run_examinator()

        while True:
            try:
                repeat = input("Chcete test zopakovat? (Y/n): ").lower()

                if repeat == "y":
                    break
                elif repeat == "n":
                    exit(0)
            except ValueError:
                print("Zadejte platný vstup (Y/n): ")
