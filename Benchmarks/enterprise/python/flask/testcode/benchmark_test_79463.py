# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import re
from app_runtime import db


def BenchmarkTest79463():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = str(db_value).split(',')
    data = ','.join(parts)
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
