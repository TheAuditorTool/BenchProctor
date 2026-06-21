# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest36330():
    ua_value = request.headers.get('User-Agent', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return jsonify({"result": "success"})
