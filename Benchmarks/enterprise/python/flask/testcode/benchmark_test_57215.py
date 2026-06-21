# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest57215():
    raw_body = request.get_data(as_text=True)
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    db.execute('SELECT * FROM users WHERE id = :id', {'id': data})
    return jsonify({"result": "success"})
