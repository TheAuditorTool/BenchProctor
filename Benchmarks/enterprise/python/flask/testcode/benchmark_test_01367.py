# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest01367():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(json_value),))
    return jsonify({'record': str(record)}), 200
