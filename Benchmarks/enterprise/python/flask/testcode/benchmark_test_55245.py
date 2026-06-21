# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest55245():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return jsonify({'secret': str(secret)}), 200
