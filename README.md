# Отправка сообщений в websocket

- **ws_server.py** асинхронный websocket сервер. Передаваемые параметры: порт и условие фильтрации.
- **ws_client.py** асинхронный websocket клиент для тестирования. Передаваемые параметры: ip адрес сервера, порт.
- **screen-ws.service** конфигурация сервиса **systemd**
- **ws_server.sh** скрипт запуска сервиса
