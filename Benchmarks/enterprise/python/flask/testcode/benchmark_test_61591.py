# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest61591():
    field_value = request.form.get('field', '')
    data = coalesce_blank(field_value)
    processed = data[:64]
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(processed),))
    return jsonify({'record': str(record)}), 200
