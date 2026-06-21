# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest22311():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = ensure_str(json_value)
    processed = data[:64]
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(processed),))
    return jsonify({"result": "success"})
