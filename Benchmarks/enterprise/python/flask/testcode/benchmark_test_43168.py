# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request
from app_runtime import db


def BenchmarkTest43168():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '%s' % (db_value,)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return jsonify({"result": "success"})
