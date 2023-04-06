import flask
from flask import jsonify,request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

cricket = [{"id":1,"name":"dhoni"},{"id":2,"name":"kohli"},{"id":3,"name":"rohith"}]
@app.route('/',methods=['GET'])
def home():
    return "welcome to my python programming"

@app.route('/players',methods=['GET'])
def home2():
    return jsonify(cricket)

@app.route('/players_id',methods=['GET'])
def home3():
    if 'id' in request.args:
        id = int (request.args['id'])
    else:
        return "Error, No such Feald"

    results = []

    for data in cricket:

        if data ["id"] == id:
            results.append(data)

        return jsonify (results)

app.run ()
