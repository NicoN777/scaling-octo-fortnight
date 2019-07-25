from flask import Flask, jsonify
import json

app = Flask(__name__)

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def serialize(self):
        return {
                'name': self.name,
                'age': self.age,
                'weight': self.weight
        }

#Fake data
toasty = Dog('Toasty', 2, 75)
pika = Dog('Pika', 1, 50)

items = [toasty, pika]

@app.route('/dogs')
def list_items():
    return jsonify(dogs=[dog.serialize() for dog in items])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
