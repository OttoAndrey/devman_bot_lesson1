import os

import requests
import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()

    tg_bot_token = os.getenv('TG_BOT_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    dvmn_token = os.getenv('DVMN_TOKEN')

    bot = telegram.Bot(token=tg_bot_token)
    headers = {'Authorization': f'Token {dvmn_token}'}
    params = {'timestamp': None}
    url = 'https://dvmn.org/api/long_polling/'

    while True:
        try:
            response = requests.get(url, headers=headers, params=params, timeout=90)
            response_data = response.json()

            if response_data['status'] == 'found':
                attempts = response_data['new_attempts'][0]
                if attempts['is_negative']:
                    answer = 'К сожалению, в работе нашлись ошибки :('
                else:
                    answer = 'Всё ок, можно приступать к след. уроку!'

                text = f'У вас проверили работу "{attempts["lesson_title"]}".' \
                       f'\n\n{answer}' \
                       f'\n\nhttps://dvmn.org{attempts["lesson_url"]}'
                bot.send_message(chat_id=chat_id, text=text)
                params = {'timestamp': response_data['last_attempt_timestamp']}

            elif response_data['status'] == 'timeout':
                params = {'timestamp': response_data['timestamp_to_request']}
        except requests.exceptions.ReadTimeout:
            continue
        except requests.exceptions.ConnectionError:
            continue


if __name__ == '__main__':
    main()
