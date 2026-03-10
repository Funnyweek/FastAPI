# CRUD Student (FastAPI)

Реализация CRUD для сущности **Student** на FastAPI без базы данных (данные в памяти).

## Запуск

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Документация API: **http://127.0.0.1:8000/docs**

## Поля студента

| Поле   | Тип    | Валидация              |
|--------|--------|------------------------|
| id     | int    | автоинкремент          |
| name   | str    | минимум 2 символа     |
| age    | int    | от 16 до 60            |
| email  | str    | валидный email         |
| course | int    | от 1 до 6              |

## Эндпоинты

| Метод  | URL              | Описание |
|--------|------------------|----------|
| GET    | `/students`      | Список всех. Фильтр: `?course=1` … `?course=6` |
| GET    | `/students/{id}` | Один студент (404 если не найден) |
| POST   | `/students`      | Создать студента (**201**) |
| PUT    | `/students/{id}` | Полное обновление |
| PATCH  | `/students/{id}` | Частичное обновление |
| DELETE | `/students/{id}` | Удалить (**204**) |

## Примеры

```bash
# Создать студента
curl -X POST http://127.0.0.1:8000/students \
  -H "Content-Type: application/json" \
  -d '{"name": "Иван Петров", "age": 20, "email": "ivan@example.com", "course": 2}'

# Список с фильтром по курсу
curl "http://127.0.0.1:8000/students?course=2"

# Получить одного
curl http://127.0.0.1:8000/students/1

# Частичное обновление (PATCH)
curl -X PATCH http://127.0.0.1:8000/students/1 \
  -H "Content-Type: application/json" \
  -d '{"course": 3}'

# Удалить
curl -X DELETE http://127.0.0.1:8000/students/1
```
