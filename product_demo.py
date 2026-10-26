from pydantic import BaseModel, ValidationError

class Product(BaseModel):
    name: str              # обов'язкове поле
    price: float           # обов'язкове поле
    in_stock: bool = True  # необов'язкове, є значення за замовчуванням
    color: str = "White"

# 1) створення з іменованих аргументів
p = Product(name="Чашка", price=120)
print(p)
print(p.name, p.price, p.in_stock, p.color)

# 2) створення зі словника (так виглядають дані з JSON)
data = {"name": "Ручка", "price": "12"}
p2 = Product.model_validate(data)
print(p2.price, type(p2.price))   # 12.0 <class 'float'>

# 3) назад у dict і в JSON-рядок
print(p2.model_dump())
print(p2.model_dump_json())



# 4) погані дані -> ValidationError
try:
    Product(name="Зошит", price="дорого")
except ValidationError as e:
    for err in e.errors():
        print(err["loc"], err["msg"])
