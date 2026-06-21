# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest75577():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    db.execute('SELECT * FROM users WHERE id = :id', {'id': json_value})
    return jsonify({"result": "success"})
