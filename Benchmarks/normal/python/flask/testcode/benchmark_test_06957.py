# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import jsonify
from app_runtime import db


def BenchmarkTest06957():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = db_value if db_value else 'default'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
