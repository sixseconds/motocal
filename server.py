from flask import Flask, redirect, request
from flask_cors import CORS
from tinydb import TinyDB, Query

app = Flask(__name__)
CORS(app)

db = TinyDB('database.json')
entry = Query()

@app.route('/savedata', methods=["POST"])
def savedata():
    data = request.form.get('datachar')
    id = str(len(db)+1)
    db.insert({"id":id, "datachar": data})
    return id

@app.route('/getdata', methods=["POST"])
def getdata():
    data = db.search(entry.id == request.form.get('id'))
    send = data[0]["datachar"]
    return send


if __name__ == "__main__":
    app.run(debug=False, port=5000)