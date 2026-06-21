# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest28536():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})
