from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
contacts = {1: {"name": "Оля", "city": "Львів"}}

class Contact(BaseModel):         # повний об'єкт — для PUT
    name: str
    city: str = "Київ"

class ContactPatch(BaseModel):    # усі поля необов'язкові — для PATCH
    name: str | None = None
    city: str | None = None

def get_or_404(contact_id: int) -> dict:
    if contact_id not in contacts:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contacts[contact_id]

@app.patch("/contacts/{contact_id}")
def update_contact(contact_id: int, data: ContactPatch):
    contact = get_or_404(contact_id)
    contact.update(data.model_dump(exclude_unset=True))  # лише надіслане
    return contact

@app.delete("/contacts/{contact_id}", status_code=204)
def delete_contact(contact_id: int):
    get_or_404(contact_id)
    del contacts[contact_id]                   # тіла відповіді немає
