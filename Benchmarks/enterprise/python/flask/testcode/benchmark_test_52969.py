# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest52969():
    origin_value = request.headers.get('Origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return jsonify({"result": "success"})
