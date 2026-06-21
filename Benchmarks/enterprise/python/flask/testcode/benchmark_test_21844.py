# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest21844():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})
