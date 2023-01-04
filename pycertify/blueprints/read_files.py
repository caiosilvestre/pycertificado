import json
import os

def read_json(json_file):
    with open(json_file, 'r', encoding='utf8') as f:
        return json.load(f)

def read_all_test():
    tests = os.listdir('./pycertify/provas/')
    return tests

def read_question(prova, question, idioma = 'en-us'):
    test_file = os.listdir(f'./pycertify/provas/{prova.lower()}/{idioma}')[0]
    path = f'./pycertify/provas/{prova.lower()}/{idioma}/{test_file}'
    question = read_json(path)[str(question)]
    return question

def read_answer(prova, question):
    test_file = os.listdir(f'./pycertify/provas/{prova.lower()}/en-us')[0]
    path = f'./pycertify/provas/{prova.lower()}/en-us/{test_file}'
    question= read_json(path)[str(question)]
    letter_correct_answer = question['correct_answer'].keys()
    for letter, value in question['correct_answer'].items():
        correct_answer = value
        letter_correct_answer = letter
    
    return letter_correct_answer,correct_answer