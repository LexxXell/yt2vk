**YT2VK (YouTube to VKontakte)**

Установить в кронтаб расписание запуска 
```
docker-compose -f <путь к файлу docker-compose.yml> up -d
```
Скрипт будет по расписанию постить в сообщество VK предпоследнее видео с YouTube канала.

**Ссылка на получение access_token**
```
https://oauth.vk.com/authorize?client_id=7983428&redirect_uri=https://oauth.vk.com/blank.html&display=page&scope=wall,offline&response_type=token&v=5.131
```