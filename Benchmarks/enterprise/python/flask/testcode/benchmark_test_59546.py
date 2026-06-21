# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest59546():
    host_value = request.headers.get('Host', '')
    db.execute('SELECT * FROM users WHERE id = ?', (host_value,))
    return jsonify({"result": "success"})
