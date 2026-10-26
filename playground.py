from pydantic import BaseModel, ValidationError
class Pet(BaseModel):
    name: str 
    species: str
    age: int
    vaccinated: bool = False

Dog = Pet(name="Diggie", species="Dog", age=10)
print(Dog)

RawPets = [
    {"name":"102", "age":"Ten", "species":"Test"},
    {"name":"Test1", "age":"22", "species":"Test"},
    {"name":"test2", "age":"10", "species":"Test"},
    {"name":"Hok", "age":"t22", "species":"Test"},
    {"name":"Grock", "age":"two",}
]

valid = []

for i, raw in enumerate(RawPets, start=1):
    try:
        pet = Pet.model_validate(raw)
        valid.append(pet)
        print("All Ok")
    except ValidationError as e:
        print("Error")
        for err in e.errors():
            print(f"Error in {err}")

