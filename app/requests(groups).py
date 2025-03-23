import requests

'''
Примеры клиентких запросов с помощью создания отдельного файла "requests(groups).py".
Реализованы запросы: Create, Read, Update, Delete. Для работы с группами.
'''

# URL сервера
url = "http://127.0.0.1:6080/api/v1/group/"

def create_group(title, description, contacts):
    #Создает новую группу.
    data = {
        "title": title,
        "description": description,
        "contacts": contacts
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print("Создан контакт:", response.json())
        return response.json()
    else:
        print(f"Ошибка: сервер вернул статус {response.status_code}", response.text)
        return None

def get_groups():
    # Получает список всех групп.
    response = requests.get(url)
    if response.status_code == 200:
        print("Данные о контактах:", response.json())
        return response.json()
    else:
        print(f"Ошибка: сервер вернул статус {response.status_code}", response.text)
        return None

def update_group(group_id, title=None, description=None, contacts=None):
    # Обновляет информацию о группе.
    data = {}
    if title:
        data["title"] = title
    if description:
        data["description"] = description
    if contacts:
        data["contacts"] = contacts

    response = requests.put(f"{url}{group_id}", json=data)
    if response.status_code == 200:
        print("Обновлены данные о контакте:", response.json())
        return response.json()
    else:
        print(f"Ошибка: сервер вернул статус {response.status_code}", response.text)
        return None

def delete_group(group_id):
    # Удаляет группу по ID.
    response = requests.delete(f"{url}{group_id}")
    if response.status_code == 200:
        print("Данные о группе были удалены:", group_id)
        return True
    else:
        print(f"Ошибка: сервер вернул статус {response.status_code}", response.text)
        return False

# Играйтесь с запросами убирая или вставляя комментарии
if __name__ == "__main__":

    # Создание группы
    new_group = create_group(
        title="Friends",
        description="My close friends",
        contacts=[1, 2, 3]
    )

    if new_group:
        group_id = new_group["id"]
        # # Обновление группы
        update_group(group_id, title="Best Friends", description="My best friends")
        # # Получение списка групп
        get_groups()

        # # Удаление группы
        # delete_group(group_id)
        # # Получение списка групп
        # get_groups()