# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest62967():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})
