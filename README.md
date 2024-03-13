# Описание
__Приложение для создания встреч__
## Дополнительное описание
```
* При создании пользователя не нужно использовать 
подтверждение по почте. Пользователи состоят в организациях. 
Одно мероприятие могут организовывать несколько организаций. 
Настроить панель администратора (добавить фильтрацию и поиск),
при просмотре мероприятия выводить превью изображения. Вывод 
информации и создание записей по api доступно только зарегистрированным
пользователям. При создании мероприятия необходимо использовать sleep 60 секунд 
и данный запрос не должен быть блокирующим.

```
## Конечные точки
```
1.	Создать проект и приложение на Django Rest Framework >= 3.12 (Django > =3.2).
2.	Реализовать возможность хранения номера телефона пользователя.
3.	Использовать email и пароль при создании и авторизации пользователя.
4.	Использовать JWT Token для аутентификации пользователя.
5.	Создать модель Организации со следующими полями: title, description, address, postcode.
6.	Создать модель Мероприятия со следующими полями: title, description, organizations, image, date.
7.	Создать чат между пользователями использую технологию Web Socket.
8.	Использовать для запуска проекта Docker.
 
```
## Конечные точки
```
* Создание организации 'api/create-organization/'
* Создание мероприятия 'api/create-event/'
* Вывод мероприятия с информацией о всех действующих
 пользователей, которые участвуют в организации мероприятия
 с разбивкой по организациям 'api/events/<int:event_id>/'
* Создание юзера 'api/create-user/'
* Все мероприятия 'api/all/' (Есть фильтрация и пагинация)
* Получение JWT-Token 'api/token/'
* Обновление JWT-Token 'api/token/refresh/'
* Чат между сотрудниками 'ws/chat/<str:room_name>/' (WebSocket)
* Админ панель 'admin/' (Добавлен поиск, фильтрация, предпросмотр изображений)
 
```
## Прочее
```
* При создании мероприятия необходимо использовать sleep 60 секунд 
 и данный запрос не должен быть блокирующим -- Реализовано с помощью Celery и Redis.
* Для чата есть html страница (chat.html)
```
![alt text](other/chat.jpg)
## Подготовка и запуск проекта
#### Клонирование репозитория
Склонируйте репозиторий на локальную машину:
```bash
git clone https://github.com/sixscale/test_spb_gby
```
#### Подготовка Docker
##### Шаг 1. Скачайте и установите Docker
```
https://www.docker.com/products/docker-desktop/
```
#### Запуск проекта
##### Необходимо прописать в терминале команду для Docker:
```bash
docker-compose up --build
```
#### Альтернативный вариант
##### Шаг 1. Необходимо перейти в директорию проекта через консоль:
```bash
cd django_test_stripe
```
##### Шаг 2. Прописать команду для Docker:
```bash
docker-compose up --build
```
## Используемый стек
```
Python, Django Rest Framework, SQLite, Celery, Redis, Daphne
```
