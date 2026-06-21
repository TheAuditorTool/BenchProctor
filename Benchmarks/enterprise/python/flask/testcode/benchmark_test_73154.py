# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import re
from app_runtime import db


def BenchmarkTest73154():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if re.search('[a-zA-Z0-9_-]+', str(db_value)):
        return jsonify({'validated': str(db_value)}), 200
    return jsonify({"result": "success"})
