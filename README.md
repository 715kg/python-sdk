[![PyPI version](https://badge.fury.io/py/gosms-ru-client.svg)](https://badge.fury.io/py/gosms-ru-client)
[![Python versions](https://img.shields.io/pypi/pyversions/gosms-ru-client.svg)](https://pypi.org/project/gosms-ru-client/)
[![Downloads](https://static.pepy.tech/badge/gosms-ru-client)](https://pepy.tech/project/gosms-ru-client)
[![License](https://img.shields.io/pypi/l/gosms-ru-client.svg)](https://github.com/Gosms-ru/python-sdk/blob/master/LICENSE)

# GoSMS Python SDK
🐍 Python SDK for GoSMS.ru API – A lightweight and efficient library for interacting with the GoSMS.ru SMS 
gateway. Send SMS, check balances, track delivery statuses, and manage contacts with ease.


## Установка

```bash
pip install gosms-ru-client
```

## Использование

### Отправка SMS

```python
from gosms_ru_client import GoSMSClient

# Инициализация клиента
client = GoSMSClient(api_key="ваш_api_ключ")

# Отправка SMS
try:
    response = client.send_sms(
        phone_number="79999999999",
        message="Тестовое сообщение",
        device_id="device_id",  # опционально
        to_sim=1,  # опционально
        callback_id="callback_id"  # опционально
    )
    print(response)
except GoSMSError as e:
    print(f"Ошибка: {e}")
```

## Обработка ошибок

Пакет предоставляет следующие классы исключений:

- `GoSMSError` - базовый класс для всех исключений
- `GoSMSAuthError` - ошибка аутентификации
- `GoSMSRequestError` - ошибка при выполнении запроса
- `GoSMSValidationError` - ошибка валидации данных

## Требования

- Python 3.7+
- requests>=2.25.0

## Лицензия

MIT

## Документация

Полная документация API доступна на сайте: https://docs.gosms.ru/
