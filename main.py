from itertools import count
from statistics import mean

import requests
from environs import Env
from tabulate import tabulate


def predict_salary(salary_from, salary_to):
    if salary_from == salary_to == 0:
        return None
    if salary_from and salary_to:
        return mean([salary_from, salary_to])
    if not salary_to:
        return salary_from * 1.2
    if not salary_from:
        return salary_to * 0.8


def get_vacancies_count_hh(lang: str) -> int:
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


def fetch_vacancies_hh(lang: str):
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


def predict_rub_salary_hh(vacancy: dict):
    salary = vacancy['salary']
    if salary['currency'] != 'RUR':
        return None
    return predict_salary(salary['from'], salary['to'])


def get_average_salary_hh(lang: str):
    lang_jobs_salaries = tuple(
        filter(
            lambda x: x is not None,
            map(predict_rub_salary_hh, fetch_vacancies_hh(lang))
        )
    )
    jobs_avg_salary = {
        'Язык программирования': lang,
        'Вакансий найдено': get_vacancies_count_hh(lang),
        'Вакансий обработано': len(lang_jobs_salaries),
        'Средняя зарплата': int(mean(lang_jobs_salaries)),
    }
    return jobs_avg_salary


def get_table_hh(prog_langs: list[str]):
    langs_jobs = list(map(get_average_salary_hh, prog_langs))
    return tabulate(langs_jobs, headers='keys', tablefmt="grid")


def get_vacancies_count_sj(secret_key: str, lang: str) -> int:
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': secret_key,
    }
    payload = {
        'catalogues': 48,
        'keyword': f'программист {lang}',
        'town': 4,
        'period': 0,
    }
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    return response.json()['total']


def fetch_vacancies_sj(secret_key: str, lang: str):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': secret_key,
    }
    for page in count(0):
        payload = {
            'catalogues': 48,
            'keyword': f'программист {lang}',
            'town': 4,
            'period': 0,
            'count': 100,
            'page': page,
        }
        response = requests.get(url, headers=headers, params=payload)
        response.raise_for_status()
        jobs = response.json()['objects']

        if not jobs:
            break

        yield from jobs


def predict_rub_salary_sj(job: dict):
    if job['currency'] != 'rub':
        return None
    return predict_salary(job['payment_from'], job['payment_to'])


def get_average_salary_sj(lang: str):
    env = Env()
    env.read_env()
    secret_key = env('SUPERJOB_SECRET_KEY')
    lang_jobs_salaries = tuple(
        filter(
            lambda x: x is not None,
            map(predict_rub_salary_sj, fetch_vacancies_sj(secret_key, lang))
        )
    )
    jobs_avg_salary = {
        'Язык программирования': lang,
        'Вакансий найдено': get_vacancies_count_sj(secret_key, lang),
        'Вакансий обработано': len(lang_jobs_salaries),
        'Средняя зарплата': int(mean(lang_jobs_salaries)),
    }
    return jobs_avg_salary


def get_table_sj(prog_langs: list[str]):
    langs_jobs = list(map(get_average_salary_sj, prog_langs))
    return tabulate(langs_jobs, headers='keys', tablefmt="grid")


if __name__ == '__main__':
    programming_languages = [
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
    print('\nHeadHunter Moscow')
    print(get_table_hh(programming_languages))
    print('\nSuperJob Moscow')
    print(get_table_sj(programming_languages))
