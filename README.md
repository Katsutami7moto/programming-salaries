# programming-salaries
Count average salaries for programmer jobs by different languages.

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
| JavaScript              |               1042 |                   913 |             182499 |
+-------------------------+--------------------+-----------------------+--------------------+
| Python                  |                602 |                   511 |             199356 |
+-------------------------+--------------------+-----------------------+--------------------+
| Java                    |                426 |                   369 |             210257 |
+-------------------------+--------------------+-----------------------+--------------------+
| C++                     |                382 |                   356 |             180126 |
+-------------------------+--------------------+-----------------------+--------------------+
| C#                      |                296 |                   267 |             189361 |
+-------------------------+--------------------+-----------------------+--------------------+
| TypeScript              |                337 |                   271 |             220101 |
+-------------------------+--------------------+-----------------------+--------------------+
| Go                      |                178 |                   151 |             228184 |
+-------------------------+--------------------+-----------------------+--------------------+
| Swift                   |                 86 |                    79 |             245765 |
+-------------------------+--------------------+-----------------------+--------------------+
| Ruby                    |                 45 |                    35 |             219514 |
+-------------------------+--------------------+-----------------------+--------------------+
| Scala                   |                 23 |                    16 |             306562 |
+-------------------------+--------------------+-----------------------+--------------------+

SuperJob Moscow
+-------------------------+--------------------+-----------------------+--------------------+
| Язык программирования   |   Вакансий найдено |   Вакансий обработано |   Средняя зарплата |
+=========================+====================+=======================+====================+
| JavaScript              |                 56 |                    40 |             182200 |
+-------------------------+--------------------+-----------------------+--------------------+
| Python                  |                 40 |                    27 |             207685 |
+-------------------------+--------------------+-----------------------+--------------------+
| Java                    |                 19 |                    14 |             260857 |
+-------------------------+--------------------+-----------------------+--------------------+
| C++                     |                 20 |                    13 |             183538 |
+-------------------------+--------------------+-----------------------+--------------------+
| C#                      |                 14 |                    12 |             227500 |
+-------------------------+--------------------+-----------------------+--------------------+
| TypeScript              |                 15 |                     9 |             339444 |
+-------------------------+--------------------+-----------------------+--------------------+
| Go                      |                  8 |                     5 |             287600 |
+-------------------------+--------------------+-----------------------+--------------------+
| Swift                   |                  3 |                     2 |             240000 |
+-------------------------+--------------------+-----------------------+--------------------+
| Ruby                    |                  5 |                     3 |             243333 |
+-------------------------+--------------------+-----------------------+--------------------+
| Scala                   |                  5 |                     5 |             468000 |
+-------------------------+--------------------+-----------------------+--------------------+
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
