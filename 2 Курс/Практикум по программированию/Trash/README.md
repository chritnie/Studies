Пунтк 2 представлен в файлах server.py и client.py
2. Модифицировать простой эхо-сервер таким образом, чтобы при подключении клиента создавался новый поток, в котором происходило взаимодействие с ним.
Новые потоки для каждого клиента создаются тут

![image](https://user-images.githubusercontent.com/58771506/135753826-5f9ade63-ed2e-45c6-9194-2c50f09219ff.png)

Результат подключения клиентов представлен здесь

![image](https://user-images.githubusercontent.com/58771506/135753880-9f2581f3-1ae4-4cbe-8d82-2d89ed30283e.png)

![image](https://user-images.githubusercontent.com/58771506/135753897-db6e81cb-be17-450c-8e87-1ae4ca497e8f.png)

![image](https://user-images.githubusercontent.com/58771506/135753930-d60638a6-e92d-405c-87f3-19f2ec1ff9a4.png)

3. Реализовать простой чат сервер на базе сервера аутентификации. Сервер должен обеспечивать подключение многих пользователей одновременно, отслеживание имен пользователей, поддерживать историю сообщений и пересылку сообщений от каждого пользователя всем остальным.
Чат реализован на TCP сокетах
О клиентах следующие данные: информация об IP клиента хранится в зашифрованном виде, логин, пароль тоже в зашифрованном виде
Они хранятся построчно в csv файле
история сообщений хранится в файле .csv
Регистрация клиента

![image](https://user-images.githubusercontent.com/58771506/135754074-b5fe4214-f8d5-43e3-a46f-43381f37acdb.png)

РЕгистрация второго клиента

![image](https://user-images.githubusercontent.com/58771506/135754111-cabffe3a-a3f0-4929-8899-96187d890a11.png)

Файл регистрации теперь выглядит так clients.csv

![image](https://user-images.githubusercontent.com/58771506/135754122-d96c96f7-4632-4d3e-9706-3e34b4f37505.png)

![image](https://user-images.githubusercontent.com/58771506/135754137-824bb5b0-a4ac-4a53-88fd-f95980892b5a.png)

Посмотрим что выводит сервер

![image](https://user-images.githubusercontent.com/58771506/135754211-ebcc6e38-3fdb-4618-ab12-54c4b02a3f8f.png)

Посмотрим как выглядит переписка у пользователей и сервера

![image](https://user-images.githubusercontent.com/58771506/135754287-2efb14be-00ae-4f93-b105-70e3e20029df.png)

![image](https://user-images.githubusercontent.com/58771506/135754301-6f4f33a5-ca0d-4b9e-96a3-0ec991ca9492.png)

![image](https://user-images.githubusercontent.com/58771506/135754310-709a50b2-f596-48c4-83ac-5680082123d2.png)

История сообщений

![image](https://user-images.githubusercontent.com/58771506/135754545-b4a7dbb1-1259-4835-b4b2-2ef456fc2266.png)

4. Реализовать сервер с управляющим потоком. При создании сервера прослушивание портов происходит в отдельном потоке, а главный поток программы в это время способен принимать команды от пользователя. Необходимо реализовать следующие команды:
Отключение сервера (завершение программы) командой shutdown

![image](https://user-images.githubusercontent.com/58771506/135754582-fdd19725-daae-4e59-81ca-f3de72868cf8.png)

Пауза (остановка прослушивание порта) командами ключения и отключения stop listen start listen

![image](https://user-images.githubusercontent.com/58771506/135754385-43794d43-9dba-495f-a8cd-8e81d74a08ce.png)

У клиента ничего не происходит, он ожидает соединения, так как мы запретили подключения
Если мы введем start listen то клиент сразу подключится

![image](https://user-images.githubusercontent.com/58771506/135754425-f3507791-564c-4c72-a983-f78b5b821cd0.png)

![image](https://user-images.githubusercontent.com/58771506/135754432-a2c0db99-6869-438b-9566-4d8b279d4bb8.png)

Показ логов выключается и включается командами stop log start log

![image](https://user-images.githubusercontent.com/58771506/135754459-3f83d3b4-ce9d-435c-b13e-4dc530d0517a.png)

Очистка логов очищается сам файл логов и консоль командой clear log

![image](https://user-images.githubusercontent.com/58771506/135754484-d66fb4c9-94c3-4f73-a75d-b61a1fd6c30b.png)

![image](https://user-images.githubusercontent.com/58771506/135754491-3e6e96b8-ad2b-4d57-8541-152b5bea44da.png)

Очистка файла идентификации выполняется командой clear file

![image](https://user-images.githubusercontent.com/58771506/135754513-9865535a-b75b-4834-8ff7-fe9d97d45905.png)

![image](https://user-images.githubusercontent.com/58771506/135754522-a8a5f8f4-9953-464d-8365-a3525444c4fb.png)



