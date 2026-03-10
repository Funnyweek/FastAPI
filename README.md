# CRUD Student (Django + DRF)

## Запуск

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

API: **http://127.0.0.1:8000/**

## Эндпоинты

| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/students/` | Список всех студентов. Фильтр: `?course=1` … `?course=6` |
| GET | `/students/{id}/` | Один студент (404 если не найден) |
| POST | `/students/` | Создать студента (201) |
| PUT | `/students/{id}/` | Полное обновление |
| PATCH | `/students/{id}/` | Частичное обновление |
| DELETE | `/students/{id}/` | Удалить (204) |

## Валидация

- **name** — строка, минимум 2 символа  
- **age** — число от 16 до 60  
- **email** — валидный email  
- **course** — число от 1 до 6  

**id** задаётся автоматически (автоинкремент).

## Примеры

```bash
# Создать студента
curl -X POST http://127.0.0.1:8000/students/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Иван Петров", "age": 20, "email": "ivan@example.com", "course": 2}'

# Список с фильтром по курсу
curl "http://127.0.0.1:8000/students/?course=2"

# Получить одного
curl http://127.0.0.1:8000/students/1/

# Частичное обновление (PATCH)
curl -X PATCH http://127.0.0.1:8000/students/1/ \
  -H "Content-Type: application/json" \
  -d '{"course": 3}'

# Удалить
curl -X DELETE http://127.0.0.1:8000/students/1/
```
