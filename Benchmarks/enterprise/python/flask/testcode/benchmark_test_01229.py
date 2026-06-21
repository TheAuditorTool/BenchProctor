# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest01229():
    ua_value = request.headers.get('User-Agent', '')
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(ua_value),))
    return jsonify({"result": "success"})
