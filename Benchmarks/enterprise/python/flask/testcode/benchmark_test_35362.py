# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest35362():
    header_value = request.headers.get('X-Custom-Header', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return jsonify({"result": "success"})
