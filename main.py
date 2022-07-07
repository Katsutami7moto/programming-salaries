import json
from itertools import count
from statistics import mean

import requests
from environs import Env


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


def predict_salary(salary_from, salary_to):
    if salary_from == salary_to == 0:
        return None
    if salary_from and salary_to:
        return mean([salary_from, salary_to])
    if not salary_to:
        return salary_from * 1.2
    if not salary_from:
        return salary_to * 0.8


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
        "vacancies_found": get_vacancies_count_hh(lang),
        "vacancies_processed": len(lang_jobs_salaries),
        "average_salary": int(mean(lang_jobs_salaries)),
    }
    return jobs_avg_salary


def main_hh(prog_langs: list[str]):
    langs_jobs = dict(zip(prog_langs, map(get_average_salary_hh, prog_langs)))
    print(json.dumps(langs_jobs, indent=4, ensure_ascii=False))


def predict_rub_salary_sj(job: dict):
    if job['currency'] != 'rub':
        return None
    return predict_salary(job['payment_from'], job['payment_to'])


def get_job_infos_sj():
    env = Env()
    env.read_env()
    secret_key = env('SUPERJOB_SECRET_KEY')
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': secret_key,
    }
    payload = {
        'catalogues': 48,
        'keyword': 'программист',
        'town': 4,
    }
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    raw_jobs = response.json()
    jobs = raw_jobs['objects']
    infos = []
    for job in jobs:
        name = job["profession"]
        town = job["town"]["title"]
        salary = predict_rub_salary_sj(job)
        infos.append(f'{name}, {town}, {salary}')
    return infos


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
    for info in get_job_infos_sj():
        print(info)
