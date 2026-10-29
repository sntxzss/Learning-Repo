from pydantic import BaseModel, Field, ValidationError, field_validator

class Item(BaseModel):
    title: str = Field(min_length=1, max_length=40)
    qty: int = Field(ge=1, le=5)     # від 1 до 99 штук
    price: float = Field(gt=0)        # строго більше нуля

class Order(BaseModel):
    customer: str = Field(min_length=2)
    items: list[Item]                 # список вкладених моделей
    promo: str = ""
    @field_validator("promo")
    @classmethod
    def check_promo(cls, v: str) -> str:
        v = v.strip().upper()
        if v and not v.startswith("SALE"):
            raise ValueError("промокод має починатися з SALE")
        return v                      # завжди повертай значення!

ok = Order(customer="Оля", promo=" sale10 ",
           items=[{"title": "Чай", "qty": "1", "price": 45}])
print(ok.items[0].qty, type(ok.items[0].qty))  # 2 <class 'int'>
print(ok.promo)                                # SALE10
try:
    Order(customer="Б", promo="free",
          items=[{"title": "", "qty": 0, "price": -1}])
except ValidationError as e:
    for err in e.errors():
        print(err["loc"], "->", err["msg"])
