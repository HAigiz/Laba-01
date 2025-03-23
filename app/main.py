#Для небольшого проекта подойдет Flask, но в дальнейшем можно использовать FastAPI для более масштабного проекта
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

class Contact:
    """Класс для представления контакта."""
    def __init__(self, id, username, given_name, family_name, phone, email, birthdate):
        self.id = id
        self.username = username
        self.given_name = given_name
        self.family_name = family_name
        self.phone = phone
        self.email = email
        self.birthdate = birthdate

def contact_to_dict(contact):
    return {
        "id": contact.id,
        "username": contact.username,
        "given_name": contact.given_name,
        "family_name": contact.family_name,
        "phone": contact.phone,
        "email": contact.email,
        "birthdate": contact.birthdate
    }

contacts = []
nextn_id = 1

class Group:
    """Класс для представления группы."""
    def __init__(self, id, title, description, contacts):
        self.id = id
        self.title = title
        self.description = description
        self.contacts = contacts

def group_to_dict(group):
    return {
        "id": group.id,
        "title": group.title,
        "description": group.description,
        "contacts": group.contacts
    }

groups = []
nextg_id = 1

#   _______________________________________________________________________________
#   \__________________________________Contacts__________________________________/

@app.route('/api/v1/contact/', methods=['POST'])
def create_contact():
    global nextn_id

    data = request.json #Получение данных из HTTP-запроса

    new_contact = Contact(
        id=nextn_id,
        username=data['username'],
        given_name=data['given_name'],
        family_name=data['family_name'],
        phone=data.get('phone', []),
        email=data.get('email', []),
        birthdate=data.get('birthdate')
    )

    nextn_id += 1  # Увеличиваем ID
    contacts.append(new_contact)

    return jsonify(contact_to_dict(new_contact))

@app.route('/api/v1/contact/', methods=['GET'])
def get_contact():
    contacts_list = [contact_to_dict(contact) for contact in contacts]
    return jsonify(contacts_list)

@app.route('/api/v1/contact/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    data = request.json

    contact = next((x for x in contacts if x.id == contact_id), None)
    if not contact:
        return jsonify({"error": "Contact not found"}), 404  # Возвращаем JSON
    contact.username = data.get('username', contact.username)
    contact.given_name = data.get('given_name', contact.given_name)
    contact.family_name = data.get('family_name', contact.family_name)
    contact.phone = data.get('phone', contact.phone)
    contact.email = data.get('email', contact.email)
    contact.birthdate = data.get('birthdate', contact.birthdate)
    return jsonify(contact_to_dict(contact))
    

@app.route('/api/v1/contact/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    global contacts

    # Реализация удаления контакта из списка контактов
    for i, contact in enumerate(contacts):
        if contact.id == contact_id:
            del contacts[i]
            return jsonify({"message": "Contact was removed", "id": contact_id})
    return jsonify({"error": "Contact not found"}), 404

# Для того, чтобы посмотреть конкретный контакт можно использоваться следующий код:
# @app.route('/api/v1/contact/<int:contact_id>', methods=['GET'])
# def get_contact_by_id(contact_id):
#     for contact in contacts:
#         if contact.id == contact_id:
#             return jsonify(contact_to_dict(contact))
#     return jsonify({"error": "Contact not found"}), 404


#   _____________________________________________________________________________
#   \__________________________________Groups__________________________________/

@app.route("/api/v1/group/", methods=["POST"])
def create_group():
    global nextg_id

    data = request.json #Получение данных из HTTP-запроса

    new_group = Group(
        id=nextg_id,
        title=data['title'],
        description=data['description'],
        contacts=data.get('contacts', [])
    )

    nextg_id += 1  # Увеличиваем ID
    groups.append(new_group)

    return jsonify(group_to_dict(new_group)), 201

@app.route("/api/v1/group/", methods=["GET"])
def get_group():
    group_list = [group_to_dict(group) for group in groups]
    return jsonify(group_list)

@app.route("/api/v1/group/<int:group_id>", methods=["PUT"])
def update_group(group_id):
    data = request.json

    for group in groups:
        if group.id == group_id:
            group.title = data.get('title', group.title)
            group.description = data.get('description', group.description)
            group.contacts = data.get('contacts', group.contacts)
            return jsonify(group_to_dict(group))
    return jsonify({"error": "Group not found"}), 404  # Возвращаем JSON

@app.route("/api/v1/group/<int:group_id>", methods=["DELETE"])
def delete_group(group_id):
    global groups

    # Реализация удаления контакта из списка контактов
    for i, group in enumerate(groups):
        if group.id == group_id:
            del groups[i]
            return jsonify({"message": "Group was removed", "id": group_id})
    return jsonify({"error": "Group not found"}), 404


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=6080)