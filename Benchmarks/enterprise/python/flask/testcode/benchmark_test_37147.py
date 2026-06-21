# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest37147():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return jsonify({"result": "success"})
