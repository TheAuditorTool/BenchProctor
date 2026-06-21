# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest66455():
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})
