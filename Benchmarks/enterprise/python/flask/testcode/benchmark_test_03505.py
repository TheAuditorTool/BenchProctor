# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest03505():
    origin_value = request.headers.get('Origin', '')
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(origin_value),))
    return jsonify({"result": "success"})
