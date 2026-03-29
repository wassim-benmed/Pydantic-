# ============================================
# TP : Pydantic vs Dynamic Typing en Python
# Nom : Wassim Ben Med
# ============================================

# ----------- 1. Dynamic Typing Problem -----------

print("=== Dynamic Typing Problem ===")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Cas correct
ali = Person("Ali", 24)
print("Correct:", ali.age)

# Cas incorrect (Python accepte quand même)
ali = Person("Ali", "24")
print("Incorrect (string):", ali.age)


# ----------- 2. Solution avec Pydantic -----------

print("\n=== Pydantic Model ===")

from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    # Validation personnalisée
    @field_validator("account_id")
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError("account_id must be positive")
        return value


# ----------- 3. Création valide -----------

print("\n=== Création valide ===")

user = User(
    name="Salah",
    email="salah@gmail.com",
    account_id=12345
)

print(user)


# ----------- 4. Test erreur type -----------

print("\n=== Test erreur type ===")

try:
    user_error = User(
        name="Ali",
        email="ali@gmail.com",
        account_id="hello"  # ❌ erreur
    )
except Exception as e:
    print("Erreur détectée :", e)


# ----------- 5. Test erreur email -----------

print("\n=== Test erreur email ===")

try:
    user_error = User(
        name="Ali",
        email="ali",  # ❌ mauvais email
        account_id=123
    )
except Exception as e:
    print("Erreur détectée :", e)


# ----------- 6. Test validation personnalisée -----------

print("\n=== Test validation personnalisée ===")

try:
    user_error = User(
        name="Ali",
        email="ali@gmail.com",
        account_id=-10  # ❌ erreur
    )
except Exception as e:
    print("Erreur détectée :", e)


# ----------- 7. JSON Serialization -----------

print("\n=== JSON Serialization ===")

user = User(
    name="Ali",
    email="ali@gmail.com",
    account_id=123
)

# JSON string
json_data = user.model_dump_json()
print("JSON:", json_data)

# Python dict
dict_data = user.model_dump()
print("Dict:", dict_data)


# ----------- 8. JSON → Objet -----------

print("\n=== JSON → Objet ===")

json_str = '{"name": "Ali", "email": "ali@gmail.com", "account_id": 123}'

user_from_json = User.parse_raw(json_str)
print(user_from_json)


# ----------- 9. Comparaison Dataclass -----------

print("\n=== Dataclass (sans validation) ===")

from dataclasses import dataclass

@dataclass
class UserDC:
    name: str
    email: str
    account_id: int

# ❌ Accepte des données incorrectes
user_dc = UserDC("Ali", "ali", "hello")
print(user_dc)


# ----------- Fin -----------

print("\n=== Fin du TP ===")