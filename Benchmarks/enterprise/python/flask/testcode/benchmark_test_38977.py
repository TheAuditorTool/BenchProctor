# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest38977():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})
