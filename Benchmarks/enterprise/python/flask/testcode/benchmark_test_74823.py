# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest74823():
    origin_value = request.headers.get('Origin', '')
    db.execute('SELECT * FROM users WHERE id = ?', (origin_value,))
    return jsonify({"result": "success"})
