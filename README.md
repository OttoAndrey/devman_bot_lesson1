# Уведомления о проверке работ

Скрипт с помощью запросов к [API Devman](https://dvmn.org/api/docs/) через бота в телеграме присылает информацию
о статусе проверенных уроков.


## Запуск

Напишите боту в телеграме, чтобы начать чат.

Для запуска скриптов вам понадобится Python3.

Скачайте код с GitHub.

Установите зависимости:

`pip3 install -r requirements.txt`

Запустите скрипт с помощью команды:

`python3 main.py`

Затем бот в телеграме пришлет вам сообщение.


## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с остальными
скриптами и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Необходимые переменные:
- `DVMN_TOKEN` - ваш персональный токен в [Devman](https://dvmn.org/api/docs/)
- `TG_BOT_TOKEN` - токен вашего бота. Узнать можно у [@botfather](https://telegram.me/botfather)
- `CHAT_ID` - ваш chat_id куда бот будет отсылать вам сообщения.
Узнать можно с помощью бота [@userinfobot](https://telegram.me/userinfobot)


## Используемые библиотеки

* [requests](https://pypi.org/project/requests/) - для запросов к API

* [python-dotenv](https://pypi.org/project/python-dotenv/) - для обращения к переменным окружения

* [python-telegram-bot](https://pypi.org/project/python-telegram-bot/) - для управления ботом


## Цели проекта

Devman. Чат-боты на Python. Первый урок.

Сайт реализован в рамках курса по Django на [devman](https://dvmn.org/modules/).
