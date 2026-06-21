# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest08400():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    db.execute('UPDATE users SET name = ?', (str(data),))
    return jsonify({"result": "success"})
