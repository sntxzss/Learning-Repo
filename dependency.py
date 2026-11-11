from fastapi import FastAPI

app = FastAPI(title="Products API")

PRODUCTS = [{"id": i, "name": f"Товар {i}"} for i in range(1, 31)]

REVIEWS = [
    {"id": 1, "product_id": 1, "rating": 5, "text": "Чудово!"},
    {"id": 2, "product_id": 2, "rating": 4, "text": "Добре"},
    {"id": 3, "product_id": 3, "rating": 5, "text": "Вiддувся!"},
    {"id": 4, "product_id": 4, "rating": 3, "text": "Нормально"},
    {"id": 5, "product_id": 5, "rating": 5, "text": "Супер!"},
    {"id": 6, "product_id": 6, "rating": 2, "text": "Не задоволений"},
    {"id": 7, "product_id": 7, "rating": 4, "text": "Гарно"},
    {"id": 8, "product_id": 8, "rating": 5, "text": "Чудесно"},
    {"id": 9, "product_id": 9, "rating": 3, "text": "Середньо"},
    {"id": 10, "product_id": 10, "rating": 5, "text": "Рекомендую!"},
    {"id": 11, "product_id": 11, "rating": 4, "text": "Добре якість"},
    {"id": 12, "product_id": 12, "rating": 5, "text": "Відмінно!"},
]


