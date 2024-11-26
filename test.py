
import os


def load_questions_from_directory(directory):
    questions = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                author = file.readline().strip()
                content = file.read().strip()
    return content
content = load_questions_from_directory("Testy_zdroj_otazek")
print(content)

