# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest77945():
    field_value = request.form.get('field', '')
    db.execute('SELECT * FROM users WHERE id = ' + str(field_value))
    return jsonify({"result": "success"})
