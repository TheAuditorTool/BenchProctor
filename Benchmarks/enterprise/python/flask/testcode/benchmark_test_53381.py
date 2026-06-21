# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest53381():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json_value if json_value else 'default'
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return jsonify({"result": "success"})
