from fastapi import APIRouter, FastAPI

# --- це був би файл app/routers/students.py ---
students_router = APIRouter(prefix="/students", tags=["students"])

@students_router.get("")                 # шлях: /students
def list_students():
    return [{"id": 1, "name": "Оля"}]

@students_router.get("/{student_id}")    # шлях: /students/{student_id}
def get_student(student_id: int):
    return {"id": student_id, "name": "Оля"}

# --- це був би файл app/routers/courses.py ---
courses_router = APIRouter(prefix="/courses", tags=["courses"])

@courses_router.get("")                  # шлях: /courses
def list_courses():
    return [{"id": 1, "title": "Python"}]

# --- це був би файл app/main.py ---
app = FastAPI(title="School API")
app.include_router(students_router)
app.include_router(courses_router)
