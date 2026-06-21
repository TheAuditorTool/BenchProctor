# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest22772():
    origin_value = request.headers.get('Origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})
