# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest30062():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(json_value),))
    return jsonify({"result": "success"})
