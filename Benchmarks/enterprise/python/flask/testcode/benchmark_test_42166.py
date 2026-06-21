# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest42166():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        os.setuid(int(str(comment_value)) if str(comment_value).isdigit() else 65534)
    except OSError:
        return jsonify({'error': 'privilege drop failed'}), 500
    return jsonify({"result": "success"})
