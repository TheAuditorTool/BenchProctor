# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import base64
from flask import jsonify
from app_runtime import db


def BenchmarkTest17133():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
