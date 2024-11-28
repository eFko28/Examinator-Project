
import os
import random
import time
from datetime import datetime

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
questions = load_questions_from_directory("Testy_zdroj_otazek")
print(questions)



