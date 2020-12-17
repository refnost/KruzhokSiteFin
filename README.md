h1 Readme
>>Используется: python 3.8.6 x64, django 3.1.4.
Чтобы установить все необходимые модули, необходимо прописать следующие команды в консоль и убедиться в установке:
# pip3 install django
# pip3 install requests

В проекте используются следующие модули: time, requests, re, django.

После этих манипуляций в файле settings.py изменить значение ALLOWED_HOSTS на значение ip-адреса сервера, например: ['127.0.0.1'], а также изменить DEBUG на False.

Далее в консоли открыть директорию с приложением и прописать следующее:
# manage.py makemigrations
# manage.py migrate
# После можно запустить сервер:
# manage.py runserver {ip-адрес:port}


В веб-сервисе используются >>ИГРЫ С ВОЗРАСТНЫМ ОГРАНИЧЕНИЕМ 12+. На главной странице пользователь вводит необходимы данные в правильном формате, 
после чего на сервере выполняется алгоритм для расчета коэффициента командной игры пользователя, данные возвращаются на страничку пользователя, 
а также запрос сохраняется в БД (sqlite3). 

На страницах есть текст, который следует прочитать, чтобы корректно работать с прототипом.

! Запрос может обрабатываться достаточно долго - это зависит от скорости соединения с сервисами API.
! В случае какой либо ошибки страница профиля может не загрузиться, или же открыться страница error.

>Создать админа, чтобы посмотреть записи в БД можно командой:

# manage.py createsuperuser
далее ввести имя админа и пароль для админа.

P.S. На данный момент это лишь прототип, поэтому некоторые функции реализованы для тестирования. 
Из этого прототипа возможно создать отличный веб-сервис для определения командном и пользователя, 
также здесь довольно просто реализовать личный кабинет (реализована общая концепция личного кабинета). 
В прототипе отсутствую лишние кнопки и функции, т.к. на этом этапе разработки они не нужны. Позже дополнительные 
функции можно интегрировать, т.к проект создан с возможностью расширения его функционала.