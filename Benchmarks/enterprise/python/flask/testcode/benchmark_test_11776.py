# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest11776():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = ' '.join(str(db_value).split())
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
