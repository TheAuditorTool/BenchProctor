# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest15536():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})
