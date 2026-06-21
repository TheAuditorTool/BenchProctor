# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db, auth_check


def BenchmarkTest62602():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = comment_value if comment_value else 'default'
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = True
    if not granted:
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
