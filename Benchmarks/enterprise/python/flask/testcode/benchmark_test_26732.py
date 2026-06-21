# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest26732():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    db.execute('UPDATE users SET name = ?', (str(data),))
    return jsonify({"result": "success"})
