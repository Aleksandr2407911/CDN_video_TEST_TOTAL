<div id="header" align="center">
  <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWpyZzFrM3N6amxnNzY3a2xwb3lzZHd1Z3YxeHh5aXYxYmJmODVteCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zOvBKUUEERdNm/giphy.gif" width="3000"/>
</div>

# Домашнее задание CDNvideo: Backend

## Постановка задачи

Необходимо разработать HTTP API, с помощью которого можно:

- Добавлять/удалять в хранилище информацию о городах.
- Запрашивать информацию о городах из хранилища.
- По заданным широте и долготе точки выдавать 2 ближайших к ней города из присутствующих в хранилище.

При запросе к API на добавление нового города клиент указывает только название города, а в хранилище добавляются также координаты города. Данные о координатах можно получать из любого внешнего API.
## Установка и Запуск
### Процесс установки и запуска происходит на Windows, при необходимости будет написана нструкция для Linux.
- установите Docker по ссылке https://www.docker.com/products/docker-desktop/
- запустите Docker
- установите pgAdmin по ссылке https://www.pgadmin.org/download/pgadmin-4-windows/
- запустите pgAdmin
- установите git bash по ссылке https://gitforwindows.org/ (можно использовать bash в редакторе кода)
- создай файл .env с данными для твой базы данных по образу в [.env.example](.env.example)
- запустите git bash и по очереди введите коменды насисанные в поле ниже
```bash
git clone <URL_репозитория> # клонирование репозитория
cd <папка_репозитория> # переход в локальный репозиторий
docker-compose up --build # запуск всех сервисов
```
## Описание API

### 1. Добавление города

**POST /user/cities/**

Запрос на добавление нового города.

#### Параметры:

- `name` (string): Название города.

#### Пример запроса:

```json
{
  "name": "Москва"
}
```

#### Пример ответа::

```json
{
  "id": 1,
  "name": "Москва",
  "coordinates": {
    "latitude": 55.7558,
    "longitude": 37.6173
  }
}
```
### 2. Удаление города

**DELETE /user/cities/{city_id}**

Запрос на добавление нового города.

#### Параметры:

- 'city_id' (integer): ID города.

#### Пример запроса:

```
DELETE /cities/1
```

#### Пример ответа::

```json
{
  "message": "Город успешно удален."
}
```
### 3. Получение информации о городах

**GET /user/cities/**

Запрос на получение списка всех городов.

#### Параметры:

- Параметров нет.

#### Пример запроса:

```
GET /cities/
```

#### Пример ответа::

```json
[
  {
    "id": 1,
    "name": "Москва",
    "coordinates": {
      "latitude": 55.7558,
      "longitude": 37.6173
    }
  },
  {
    "id": 2,
    "name": "Санкт-Петербург",
    "coordinates": {
      "latitude": 59.9343,
      "longitude": 30.3351
    }
  }
]
```

### 4. Поиск ближайших городов

**GET /user/nearest_cities**

Запрос на получение 2 ближайших городов по заданным координатам.

#### Параметры:

- latitude (float): Широта точки.
-  longitude (float): Долгота точки.

#### Пример запроса:

```
GET /cities/nearest?latitude=55.7558&longitude=37.6173
```

#### Пример ответа::

```json
[
  {
    "id": 1,
    "name": "Москва",
    "coordinates": {
      "latitude": 55.7558,
      "longitude": 37.6173
    }
  },
  {
    "id": 2,
    "name": "Санкт-Петербург",
    "coordinates": {
      "latitude": 59.9343,
      "longitude": 30.3351
    }
  }
]
```
- Связаться с автором: [![Telegram Badge](https://img.shields.io/badge/-telegram-blue?style=flat&logo=Telegram&logoColor=white)](https://t.me/Neighbourhood99)

