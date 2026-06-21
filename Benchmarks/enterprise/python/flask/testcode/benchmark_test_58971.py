# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest58971():
    ua_value = request.headers.get('User-Agent', '')
    db.execute('SELECT * FROM users WHERE id = ' + str(ua_value))
    return jsonify({"result": "success"})
