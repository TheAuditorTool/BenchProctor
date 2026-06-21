# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest57673():
    auth_header = request.headers.get('Authorization', '')
    data = coalesce_blank(auth_header)
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return jsonify({"result": "success"})
