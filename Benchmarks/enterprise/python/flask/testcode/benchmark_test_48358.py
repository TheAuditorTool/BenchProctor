# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
from flask import redirect
import urllib.parse
from app_runtime import db


def BenchmarkTest48358():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = (lambda v: v.strip())(db_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
