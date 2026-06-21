# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest39621():
    cookie_value = request.cookies.get('session_token', '')
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(cookie_value),))
    return jsonify({'secret': str(secret)}), 200
