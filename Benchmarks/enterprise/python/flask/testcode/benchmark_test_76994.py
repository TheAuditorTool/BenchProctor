# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest76994():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return jsonify({'secret': str(secret)}), 200
