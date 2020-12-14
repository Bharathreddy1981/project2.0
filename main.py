
from hvr import database, register, validations,total, update, delete
from flask import Flask, jsonify, request

main = Flask(__name__)
@main.route("/register_data", methods=['POST'])
def reg():
    json_data = request.get_json()
    db = database.base()
    validations_data = validations.valid(json_data)
    value = register.insert(db, json_data, validations_data)
    return jsonify(value)

@main.route("/total_data", methods=['GET'])
def list_user():
    db = database.base()
    value = total.total(db)
    return jsonify(value)


@main.route("/update_data", methods=['POST'])
def edit_user():
    json_data = request.get_json()
    db = database.base()
    validations_data = validations.valid(json_data)
    value = update.update(db, json_data, validations_data)
    return jsonify(value)

@main.route("/delete_data", methods=['POST'])
def delete_user():
    json_data = request.get_json()
    db = database.base()
    value = delete.delete(db, json_data)
    return jsonify(value)


if(__name__ == "__main__"):
   main.run(debug=True)
