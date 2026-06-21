# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest25727():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return jsonify({'record': str(record)}), 200
