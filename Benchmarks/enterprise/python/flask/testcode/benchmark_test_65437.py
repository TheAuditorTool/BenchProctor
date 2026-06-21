# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest65437():
    auth_header = request.headers.get('Authorization', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', auth_header):
        return jsonify({'error': 'forbidden'}), 400
    processed = auth_header
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return jsonify({"result": "success"})
