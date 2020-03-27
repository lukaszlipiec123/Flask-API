from flask import Flask, jsonify, abort, make_response, request
import random

app = Flask(__name__)

quasi_db = [
    {
    'id':1,
    }
]

# Zwróć losowo 1 lub 0
@app.route('/api', methods=['GET'])
def get_records():
    num = random.randint(0, 1)
    return jsonify({'result':num})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}), 404)


@app.route('/api', methods=['POST'])
def create_task():
    if not request.json:
        abort(400)
    record = {
        'id': request.json['id'],
    }
    quasi_db.append(record)
    return jsonify({'record': record}), 201


# @app.route('/<int:record_id>', methods=['GET'])
# def get_record(record_id):
#     record = [record for record in quasi_db if record['id'] == record_id]
#     if len(record) == 0:
#         abort(404)
#     return jsonify({'record': record[0]})

if __name__ == '__main__':
    app.run(debug=True)
