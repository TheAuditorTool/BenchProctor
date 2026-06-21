# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest49685():
    ua_value = request.headers.get('User-Agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return jsonify({"result": "success"})
