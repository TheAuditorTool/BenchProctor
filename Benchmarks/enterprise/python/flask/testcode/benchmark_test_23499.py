# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db, auth_check


def BenchmarkTest23499():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        granted = auth_check('resource', str(db_value))
    except Exception:
        granted = True
    if not granted:
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
