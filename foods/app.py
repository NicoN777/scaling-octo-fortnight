from flask import Flask
import json

app = Flask(__name__)

#Fake data
items = ['Hamburgers', 'Pizza', 'Ice Cream', 'Hot Dog']


@app.route('/food')
def list_items():
    return json.dumps(items)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
