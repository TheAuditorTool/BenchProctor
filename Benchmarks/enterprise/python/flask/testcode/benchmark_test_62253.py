# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest62253():
    field_value = request.form.get('field', '')
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(field_value),))
    return jsonify({'record': str(record)}), 200
