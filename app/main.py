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
        self.phone = phone
        self.email = email
        self.birthdate = birthdate

    def contact_to_dict(self):
        return {
            'id': self.id, 
            'username': self.username,
            'givenname': self.givenname,
            'familyname': self.familyname,
            'phone': self.phone.phone_to_dict() if self.phone else None,
            'email': self.email,
            'birthdate': self.birthdate.isoformat() if self.birthdate else None
        }

class Group:
    def __init__(self, id: int, title: str, description: str, contacts: list):
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
    

#   _______________________________________________________________________________
#   \__________________________________Contacts__________________________________/
@app.route('/api/v1/contact/', methods=['GET'])
def read_contact():
    contact = Contact(1, "test", "test", "test", Phone(1, 7, 9, 9), "test", date(2022, 1, 1))
    return jsonify(contact.contact_to_dict())

@app.route('/api/v1/contact/', methods=['POST'])
def create_contact():
    contact = Contact(1, "test", "test", "test", Phone(1, 7, 9, 9),"test", date(2022, 1, 1))
    return jsonify(contact.contact_to_dict())

@app.route('/api/v1/contact/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    contact = Contact(1, "deleted_test", "deleted_test", "deleted_test", Phone(0, 0, 0, 0), "deleted_test", date(1, 1, 1))
    return jsonify(contact.contact_to_dict())

@app.route('/api/v1/contact/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    contact = Contact(1, "test1", "test1", "test1", Phone(1, 8, 937, 3646337), "test1", date(2023, 6, 20))
    return jsonify(contact.contact_to_dict())


#   _____________________________________________________________________________
#   \__________________________________Groups__________________________________/
@app.route('/api/v1/group/', methods=['GET'])
def read_group():
    group = Group(1, "Test", "Test", [0, 1])
    return jsonify(group.group_to_dict())

@app.route('/api/v1/group/', methods=['POST'])
def create_group():
    group = Group(1, "Test", "Test", [0, 1])
    return jsonify(group.group_to_dict())

@app.route('/api/v1/group/<int:group_id>', methods=['DELETE'])
def delete_group(group_id):
    group = Group(1, "Deleted_Test", "Deleted_Test", [None, None])
    return jsonify(group.group_to_dict())

@app.route('/api/v1/group/<int:group_id>', methods=['PUT'])
def update_group(group_id):
    group = Group(1, "Test1", "Test1", [1, 2])
    return jsonify(group.group_to_dict())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6080)