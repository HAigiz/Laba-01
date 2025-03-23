import requests

'''
Примеры клиентских запросов с помощью создания отдельного файла "requests_contacts.py".
Реализованы запросы: Create, Read, Update, Delete. Для работы с контактами.
'''

# URL сервера
url = "http://127.0.0.1:6080/api/v1/contact/"

def create_contact(username, given_name, family_name, phone=None, email=None, birthdate=None):
    # Создает новый контакт.
    data = {
        "username": username,
        "given_name": given_name,
        "family_name": family_name,
        "phone": phone if phone else [],
        "email": email if email else [],
        "birthdate": birthdate
    }

    response = requests.post(url, json=data)
    if response.status_code == 201:
        print("Создан контакт:", response.json())
        return response.json()
    else:
        print(f"Ошибка: сервер вернул статус {response.status_code}", response.text)
        return None

def update_contact(contact_id, username=None, given_name=None, family_name=None, phone=None, email=None, birthdate=None):
    # Обновляет информацию о контакте.
    data = {}
    if username:
        data["username"] = username
    if given_name:
        data["given_name"] = given_name
    if family_name:
        data["family_name"] = family_name
    if phone:
        data["phone"] = phone
    if email:
        data["email"] = email
    if birthdate:
        data["birthdate"] = birthdate

    response = requests.put(f"{url}{contact_id}", json=data)
    if response.status_code == 200:
        print("Обновлены данные о контакте:", response.json())
        return response.json()
    else:
        print(f"Ошибка: сервер вернул статус {response.status_code}", response.text)
        return None

def get_contacts():
    # Получает список всех контактов.
    response = requests.get(url)
    if response.status_code == 200:
        print("Данные о контактах:", response.json())
        return response.json()
    else:
        print(f"Ошибка: сервер вернул статус {response.status_code}", response.text)
        return None

def delete_contact(contact_id):
    # Удаляет контакт по ID.
    response = requests.delete(f"{url}{contact_id}")
    if response.status_code == 200:
        print("Данные о контакте были удалены:", contact_id)
        return True
    else:
        print(f"Ошибка: сервер вернул статус {response.status_code}", response.text)
        return False

# Играйтесь с запросами убирая или вставляя комментарии
def main():

    # Создание контакта
    new_contact = create_contact(
        username="Matvey",
        given_name="Matuey",
        family_name="Matveyka",
        phone="89777777777",
        email="superdupermops@gmail.com",
        birthdate="15.06.2007"
    )

    if new_contact: 
        contact_id = new_contact["id"]
        # Обновление контакта
        update_contact(
            contact_id,
            phone="89641328468",
            email="acouplehoursofsleep@gmail.com"
        )
        # # Получение всех контактов
        get_contacts()
        
        # # Удаление контакта
        # delete_contact(contact_id)
        # # Получение всех контактов после удаления
        # get_contacts()

if __name__ == "__main__":
    main()