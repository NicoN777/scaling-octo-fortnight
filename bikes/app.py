from flask import Flask, request, jsonify
import json

app = Flask(__name__)

#Fake data
items = [{'Specialized': ['Langster', 'Crave']}, {'Felt': ['FR40']}]


@app.route('/bikes')
def list_items():
    return jsonify(items)

@app.route('/bikes/add', methods=['POST'])
def add_bike():
    if request.method == 'POST':
        bike = request.get_json()
        print(f'Received: {bike}', type(bike))
        brand = list(bike.keys())[0]
        model = list(bike.values())[0]
    return jsonify({'message': 'Received: {}'.format(bike), 'data':items})  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
