import json
from itertools import count
from statistics import mean

import requests
from environs import Env


def hh_get_vacancies_count(lang: str) -> int:
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


def hh_fetch_vacancies(lang: str):
    url = 'https://api.hh.ru/vacancies'
    for page in count(0):
        payload = {
            'text': f'программист {lang}',
            'area': 1,
            'period': 30,
            'only_with_salary': True,
            'page': page,
        }
        response = requests.get(url, params=payload)
        response.raise_for_status()
        raw_vacancies: dict = response.json()

        if page >= raw_vacancies['pages']:
            break

        yield from raw_vacancies['items']


def hh_predict_rub_salary(vacancy: dict):
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


def hh_get_average_salary(lang: str):
    lang_jobs_salaries = tuple(
        filter(
            lambda x: x is not None,
            map(hh_predict_rub_salary, hh_fetch_vacancies(lang))
        )
    )
    jobs_avg_salary = {
        "vacancies_found": hh_get_vacancies_count(lang),
        "vacancies_processed": len(lang_jobs_salaries),
        "average_salary": int(mean(lang_jobs_salaries)),
    }
    return jobs_avg_salary


def hh_main():
    prog_langs = [  # sorted descending by "vacancies_processed"
        'JavaScript',
        'Python',
        'Java',
        'C++',
        'C#',
        'TypeScript',
        'Go',
        'Swift',
        'Ruby',
        'Scala',
    ]
    langs_jobs = dict(zip(prog_langs, map(hh_get_average_salary, prog_langs)))
    print(json.dumps(langs_jobs, indent=4, ensure_ascii=False))


def sj_get_job_names():
    env = Env()
    env.read_env()
    secret_key = env('SUPERJOB_SECRET_KEY')
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': secret_key,
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    jobs = response.json()['objects']
    names = [job['profession'] for job in jobs]
    return names


if __name__ == '__main__':
    for name in sj_get_job_names():
        print(name)
