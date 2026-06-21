# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import jsonify
from app_runtime import db


def BenchmarkTest79072():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data, _sep, _rest = str(db_value).partition('\x00')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
