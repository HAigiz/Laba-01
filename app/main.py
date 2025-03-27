from flask import Flask, jsonify, request
from datetime import date

app = Flask(__name__)

class Phone:
    def __init__(self, TypeID: int, CountryCode: int, Operator: int, Number: int):
        self.TypeID = TypeID
        self.CountryCode = CountryCode
        self.Operator = Operator
        self.Number = Number

    def phone_to_dict(self):
        return {
            'TypeID': self.TypeID,
            'CountryCode': self.CountryCode,
            'Operator': self.Operator,
            'Number': self.Number
        }

class Contact:
    def __init__(self, id: int, username: str, givenname: str, familyname: str, phone: Phone, email: list, birthdate: date):
        self.id = id
        self.username = username
        self.givenname = givenname
        self.familyname = familyname
        self.phone = phone  # Здесь должен быть экземпляр Phone, а не класс
        self.email = email
        self.birthdate = birthdate

    def contact_to_dict(self):
        return {
            'id': self.id, 
            'username': self.username,
            'givenname': self.givenname,
            'familyname': self.familyname,
            'phone': self.phone.phone_to_dict() if self.phone else None,  # Сериализуем объект Phone
            'email': self.email,
            'birthdate': self.birthdate.isoformat() if self.birthdate else None  # Сериализуем дату
        }

class Group:
    def __init__(self, id: int, title: str, description: str, contacts: int):
        self.id = id
        self.title = title
        self.description = description
        self.contacts = contacts

    def group_to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'contacts': self.contacts
        }

@app.route('/api/v1/contact/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_contact():
    phone = Phone(1, 7, 9, 9)  # Создаем экземпляр Phone
    contact = Contact(1, 'test', 'test', 'test', phone, ['test@example.com'], date(2022, 1, 1))
    
    if request.method == 'POST':
        return jsonify(contact.contact_to_dict())
    elif request.method == 'GET':
        return jsonify(contact.contact_to_dict())
    elif request.method == 'PUT':
        contact = Contact(1, 'test', 'test', 'test', phone, ['updated@example.com'], date(2020, 6, 5))
        return jsonify(contact.contact_to_dict())
    elif request.method == 'DELETE':
        return jsonify({
            "message": "Контакт был удален",
            "contact": contact.contact_to_dict()
        })

@app.route('/api/v1/group/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_group():
    group = Group(1, 'test', 'test', 1)
    
    if request.method == 'POST':
        return jsonify(group.group_to_dict())
    elif request.method == 'GET':
        return jsonify(group.group_to_dict())
    elif request.method == 'PUT':
        group = Group(1, 'test', 'updated description', 2)
        return jsonify(group.group_to_dict())
    elif request.method == 'DELETE':
        return jsonify({
            "message": "Группа была удалена",
            "group": group.group_to_dict()
        })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6080)