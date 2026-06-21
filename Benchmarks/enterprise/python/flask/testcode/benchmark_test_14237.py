# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest14237():
    host_value = request.headers.get('Host', '')
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(host_value),))
    return jsonify({"result": "success"})
