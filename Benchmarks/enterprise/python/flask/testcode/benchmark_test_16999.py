# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest16999():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    db.execute('UPDATE users SET name = ?', (str(data),))
    return jsonify({"result": "success"})
