# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest57767():
    ua_value = request.headers.get('User-Agent', '')
    data = default_blank(ua_value)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return jsonify({"result": "success"})
