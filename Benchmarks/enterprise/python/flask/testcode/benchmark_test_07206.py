# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest07206():
    user_id = request.args.get('id', '')
    data = normalise_input(user_id)
    db.execute('SELECT * FROM "' + str(data).replace('"', '""') + '"')
    return jsonify({"result": "success"})
