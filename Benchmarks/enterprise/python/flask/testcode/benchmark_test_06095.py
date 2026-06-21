# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest06095():
    host_value = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})
