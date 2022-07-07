import pprint
import statistics

import requests


def get_vacancies(lang: str):
    url = 'https://api.hh.ru/vacancies'
    payload = {
        'text': f'программист {lang}',
        'area': 1,
        'period': 30,
        'only_with_salary': True,
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()['items']


def predict_rub_salary(vacancy: dict):
    salary = vacancy['salary']
    salary_from = salary['from']
    salary_to = salary['to']
    salary_currency = salary['currency']
    if salary_currency != 'RUR':
        return None
    if salary_from and salary_to:
        return statistics.mean([salary_from, salary_to])
    if not salary_to:
        return salary_from * 1.2
    if not salary_from:
        return salary_to * 0.8


def show_predicted_rub_salaries(lang: str):
    for vacancy in get_vacancies(lang):
        print(predict_rub_salary(vacancy))


def get_jobs_number(lang: str):
    url = 'https://api.hh.ru/vacancies'
    payload = {
        'text': f'программист {lang}',
        'area': 1,
        'period': 30,
        'only_with_salary': True,
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()['found']


def main():
    prog_langs = [
        'JavaScript',
        'Python',
        'Java',
        'TypeScript',
        'C#',
        'C++',
        'Ruby',
        'Go',
        'Swift',
        'Scala',
    ]
    jobs_numbers = dict()
    for lang in prog_langs:
        jobs_numbers[lang] = get_jobs_number(lang)
    pprint.pprint(jobs_numbers, indent=4)


if __name__ == '__main__':
    main()
    show_predicted_rub_salaries('Python')
