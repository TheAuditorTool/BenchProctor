# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest46664():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = to_text(json_value)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return jsonify({"result": "success"})
