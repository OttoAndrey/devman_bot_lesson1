import os
import time
from textwrap import dedent

import requests
import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()

    tg_bot_token = os.getenv('TG_BOT_TOKEN')
    chat_id = os.getenv('VK_CHAT_ID')
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
                attempt = response_data['new_attempts'][0]
                if attempt['is_negative']:
                    answer = 'К сожалению, в работе нашлись ошибки :('
                else:
                    answer = 'Всё ок, можно приступать к след. уроку!'

                text = f'''\
                У вас проверили работу "{attempt["lesson_title"]}".

                {answer} 

                https://dvmn.org{attempt["lesson_url"]}'''

                bot.send_message(chat_id=chat_id, text=dedent(text))
                params = {'timestamp': response_data['last_attempt_timestamp']}

            elif response_data['status'] == 'timeout':
                params = {'timestamp': response_data['timestamp_to_request']}
        except requests.exceptions.ReadTimeout:
            continue
        except requests.exceptions.ConnectionError:
            time.sleep(60)
            continue


if __name__ == '__main__':
    main()
