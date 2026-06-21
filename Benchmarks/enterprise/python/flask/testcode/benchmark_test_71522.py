# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest71522():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = ' '.join(str(json_value).split())
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return jsonify({"result": "success"})
