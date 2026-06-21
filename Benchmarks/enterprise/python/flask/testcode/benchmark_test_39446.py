# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db, auth_check


def BenchmarkTest39446():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '{}'.format(comment_value)
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = False
    if not granted:
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
