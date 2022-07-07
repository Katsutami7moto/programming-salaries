# programming-salaries
Count average salaries for programmer jobs by different languages

### How to install

Python3 should be already installed.
Download the [ZIP archive](https://github.com/Katsutami7moto/programming-salaries/archive/refs/heads/main.zip) of the code and unzip it.
Then open terminal form unzipped directory and use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```commandline
pip install -r requirements.txt
```
Before you run the script, you will need to configure an environmental 
variable:

1. Go to the unzipped directory and create a file with the name `.env` (yes, it has only the extension).
It is the file to contain environmental variables that usually store data unique to each user, thus you will need to create your own.
2. Copy and paste this to `.env` file:
```dotenv
SUPERJOB_SECRET_KEY='{superjob_secret_key}'
```
3. Log in to or sign up for [SuperJob](https://www.superjob.ru/auth/login/) website.
4. Register an app [here](https://api.superjob.ru/register) to obtain API 
   secret key. "App website" can be anything, it won't be checked.
5. Replace `{superjob_secret_key}` in `.env` file with that secret key. Key 
   has to 
   remain 
   inside `' '` quotation marks and without `{ }` curly brackets.
6. Now you can use the script.

### How to use

Run the script with this command:
```commandline
python3 main.py
```

You will see something like this:
```
HeadHunter Moscow
+-------------------------+--------------------+-----------------------+--------------------+
| Язык программирования   |   Вакансий найдено |   Вакансий обработано |   Средняя зарплата |
+=========================+====================+=======================+====================+
| JavaScript              |               1076 |                   941 |             182948 |
+-------------------------+--------------------+-----------------------+--------------------+
| Python                  |                612 |                   514 |             202525 |
+-------------------------+--------------------+-----------------------+--------------------+
| Java                    |                424 |                   362 |             213036 |
+-------------------------+--------------------+-----------------------+--------------------+
| C++                     |                389 |                   357 |             182384 |
+-------------------------+--------------------+-----------------------+--------------------+
| C#                      |                306 |                   273 |             186794 |
+-------------------------+--------------------+-----------------------+--------------------+
| TypeScript              |                342 |                   272 |             223166 |
+-------------------------+--------------------+-----------------------+--------------------+
| Go                      |                180 |                   152 |             234181 |
+-------------------------+--------------------+-----------------------+--------------------+
| Swift                   |                 90 |                    83 |             245283 |
+-------------------------+--------------------+-----------------------+--------------------+
| Ruby                    |                 51 |                    39 |             209743 |
+-------------------------+--------------------+-----------------------+--------------------+
| Scala                   |                 23 |                    16 |             281062 |
+-------------------------+--------------------+-----------------------+--------------------+

SuperJob Moscow
+-------------------------+--------------------+-----------------------+--------------------+
| Язык программирования   |   Вакансий найдено |   Вакансий обработано |   Средняя зарплата |
+=========================+====================+=======================+====================+
| JavaScript              |                 75 |                    57 |             244509 |
+-------------------------+--------------------+-----------------------+--------------------+
| Python                  |                 49 |                    35 |             220328 |
+-------------------------+--------------------+-----------------------+--------------------+
| Java                    |                 26 |                    20 |             249000 |
+-------------------------+--------------------+-----------------------+--------------------+
| C++                     |                 25 |                    17 |             221000 |
+-------------------------+--------------------+-----------------------+--------------------+
| C#                      |                 19 |                    15 |             212266 |
+-------------------------+--------------------+-----------------------+--------------------+
| TypeScript              |                 26 |                    20 |             396900 |
+-------------------------+--------------------+-----------------------+--------------------+
| Go                      |                 15 |                    12 |             342166 |
+-------------------------+--------------------+-----------------------+--------------------+
| Swift                   |                  3 |                     2 |             240000 |
+-------------------------+--------------------+-----------------------+--------------------+
| Ruby                    |                  6 |                     4 |             233500 |
+-------------------------+--------------------+-----------------------+--------------------+
| Scala                   |                 10 |                    10 |             506500 |
+-------------------------+--------------------+-----------------------+--------------------+
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
