import json
from statistics import mean

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
    return response.json()


def predict_rub_salary(vacancy: dict):
    salary = vacancy['salary']
    salary_from = salary['from']
    salary_to = salary['to']
    salary_currency = salary['currency']
    if salary_currency != 'RUR':
        return None
    if salary_from and salary_to:
        return mean([salary_from, salary_to])
    if not salary_to:
        return salary_from * 1.2
    if not salary_from:
        return salary_to * 0.8


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
    langs_jobs = dict()
    for lang in prog_langs:
        raw_lang_jobs = get_vacancies(lang)
        lang_jobs = raw_lang_jobs['items']
        lang_jobs_salaries = tuple(
            filter(
                lambda x: x is not None,
                map(predict_rub_salary, lang_jobs)
            )
        )
        jobs_avg_salary = {
            "vacancies_found": raw_lang_jobs['found'],
            "vacancies_processed": len(lang_jobs_salaries),
            "average_salary": int(mean(lang_jobs_salaries)),
        }
        langs_jobs[lang] = jobs_avg_salary
    print(json.dumps(langs_jobs, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    main()
