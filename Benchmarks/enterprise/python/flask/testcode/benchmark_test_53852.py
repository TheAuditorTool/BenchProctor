# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest53852():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    db.execute('UPDATE users SET name = ?', (str(data),))
    return jsonify({"result": "success"})
