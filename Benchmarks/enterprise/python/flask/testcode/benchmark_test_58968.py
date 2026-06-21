# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import jsonify
from app_runtime import db


def BenchmarkTest58968():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = (lambda v: v.strip())(db_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
