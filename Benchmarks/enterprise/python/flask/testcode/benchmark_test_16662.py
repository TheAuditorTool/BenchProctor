# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import re
from app_runtime import db


def BenchmarkTest16662():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = db_value if db_value else 'default'
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
