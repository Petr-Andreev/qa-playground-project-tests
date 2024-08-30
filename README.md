# Дипломный проект QA.GURU (API-тестирование)

Данный репозиторий содержит проект - API тестирование для https://qa-playground.com/ru - часть дипломной работы, выполненной в рамках обучения на курсах QA.GURU.
Проект разработан с целью продемонстрировать полученные навыки и знания в области тестирования программного обеспечения.

## 🛠 Технологии примененные в данном проекте

  
<div>
  <a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="36" height="36" alt="Python" /></a>
  <a href="https://git-scm.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/git-colored.svg" width="36" height="36" alt="Git" /></a>
  <img src="https://github.com/devicons/devicon/blob/master/icons/pytest/pytest-original-wordmark.svg" title="pytest" alt="pytest" width="40" height="40"/>&nbsp
  <img src="https://github.com/SheriffSmitter/Petstore_api/blob/main/pictures/icons/requests.png" title="requests" alt="requests" width="40" height="40"/>&nbsp
  <img src="https://img.icons8.com/?size=100&id=3tC9EQumUAuq&format=png&color=000000" title="github" alt="github" width="40" height="40"/>&nbsp
  <img src="https://camo.githubusercontent.com/e8c35be9136635c1b2e2b22b112e02ef1fb9e9434970df18d84071a2e714d3e0/68747470733a2f2f616c6c7572657265706f72742e6f72672f7075626c69632f696d672f616c6c7572652d7265706f72742e737667" title="allure" alt="allure" width="40" height="40"/>&nbsp
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pycharm/pycharm-original.svg" title="pycharm" alt="pycharm" width="40" height="40"/>&nbsp
  <img src="https://cdn-icons-png.flaticon.com/512/2111/2111646.png" title="telegram" alt="telegram" width="40" height="40"/>&nbsp     
</div>

## Список автоматизированных тест-кейсов:
1. Проверка успешного получения пользователей по заданному лимиту
2. Проверка успешного создания нового пользователя
3. Проверка успешного удаления пользователя
4. Проверка успешного изменения пользователя по заданным параметрам
5. Проверка успешного получения игр по заданному лимиту
6. Проверка успешного получения игры по названию
7. Успешное успешного получения игры по значению uuid

## Запуск тестов и получение отчета

### **Локально**

<details><summary>1. Склонировать репозиторий</summary>

```
git clone https://github.com/Petr-Andreev/qa-playground-project-tests.git
```
</details>

<details><summary>2. Создать и активировать виртуальное окружение, установить зависимости и запустить тесты</summary>

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -sv
```
</details>

<details><summary>3. Получить отчет о прохождении тестов в allure</summary>

```
allure serve allure-results
```
</details>

<details><summary>4. После выполнения команды откроется браузер с отчетом</summary>
    
<img src="resources/allure_local.png">

</details>

## <img src="https://camo.githubusercontent.com/e8c35be9136635c1b2e2b22b112e02ef1fb9e9434970df18d84071a2e714d3e0/68747470733a2f2f616c6c7572657265706f72742e6f72672f7075626c69632f696d672f616c6c7572652d7265706f72742e737667" title="allure" alt="allure" width="30" height="30"/></a>

<details><summary>Основной отчет</summary>

<img src="resources/allure_base_report.png">

</details>
<details><summary>Тесты</summary>

<img src="resources/allure_tests.png">

</details>
