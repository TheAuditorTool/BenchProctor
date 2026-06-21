# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest27541():
    field_value = request.form.get('field', '')
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    db.execute('SELECT * FROM users WHERE id = :id', {'id': data})
    return jsonify({"result": "success"})
