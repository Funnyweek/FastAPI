from typing import List, Optional

from fastapi import FastAPI, APIRouter, HTTPException, Query
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(title="Students CRUD (FastAPI)")

router = APIRouter(prefix="/students", tags=["students"])


# ----- Схемы Pydantic -----

class StudentBase(BaseModel):
    name: str = Field(..., min_length=2, description="Минимум 2 символа")
    age: int = Field(..., ge=16, le=60, description="От 16 до 60")
    email: EmailStr
    course: int = Field(..., ge=1, le=6, description="Курс от 1 до 6")


class StudentCreate(StudentBase):
    pass


class StudentUpdate(StudentBase):
    """Полное обновление (PUT)."""
    pass


class StudentPartialUpdate(BaseModel):
    """Частичное обновление (PATCH) — все поля опциональны."""
    name: Optional[str] = Field(None, min_length=2)
    age: Optional[int] = Field(None, ge=16, le=60)
    email: Optional[EmailStr] = None
    course: Optional[int] = Field(None, ge=1, le=6)


class Student(StudentBase):
    id: int


# ----- Хранилище в памяти -----

students_db: List[Student] = []
next_id: int = 1


def get_student_or_404(student_id: int) -> Student:
    for s in students_db:
        if s.id == student_id:
            return s
    raise HTTPException(status_code=404, detail="Student not found")


# ----- Эндпоинты -----

@router.get("/", response_model=List[Student])
def list_students(
    course: Optional[int] = Query(None, ge=1, le=6, description="Фильтр по курсу (1–6)"),
):
    """GET /students — список всех. Опционально ?course=1..6"""
    if course is None:
        return students_db
    return [s for s in students_db if s.course == course]


@router.get("/{student_id}", response_model=Student)
def get_student(student_id: int):
    """GET /students/{id} — один студент (404 если не найден)."""
    return get_student_or_404(student_id)


@router.post("/", response_model=Student, status_code=201)
def create_student(student_in: StudentCreate):
    """POST /students — создать студента (201)."""
    global next_id
    student = Student(id=next_id, **student_in.model_dump())
    next_id += 1
    students_db.append(student)
    return student


@router.put("/{student_id}", response_model=Student)
def update_student(student_id: int, student_in: StudentUpdate):
    """PUT /students/{id} — полное обновление."""
    student = get_student_or_404(student_id)
    student.name = student_in.name
    student.age = student_in.age
    student.email = student_in.email
    student.course = student_in.course
    return student


@router.patch("/{student_id}", response_model=Student)
def partial_update_student(student_id: int, student_in: StudentPartialUpdate):
    """PATCH /students/{id} — частичное обновление."""
    student = get_student_or_404(student_id)
    data = student_in.model_dump(exclude_unset=True)
    for field, value in data.items():
        setattr(student, field, value)
    return student


@router.delete("/{student_id}", status_code=204)
def delete_student(student_id: int):
    """DELETE /students/{id} — удалить (204 No Content)."""
    student = get_student_or_404(student_id)
    students_db.remove(student)
    return None


app.include_router(router)
