# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest26826():
    header_value = request.headers.get('X-Custom-Header', '')
    db.execute('UPDATE users SET name = ?', (str(header_value),))
    return jsonify({"result": "success"})
