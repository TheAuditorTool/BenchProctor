# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest40807():
    header_value = request.headers.get('X-Custom-Header', '')
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(header_value)))
    return jsonify({"result": "success"})
