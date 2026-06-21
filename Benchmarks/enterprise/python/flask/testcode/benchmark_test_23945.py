# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
from app_runtime import db


def BenchmarkTest23945():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
