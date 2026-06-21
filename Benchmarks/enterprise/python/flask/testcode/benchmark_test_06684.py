# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest06684():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = str(db_value).split(',')
    data = ','.join(parts)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200
