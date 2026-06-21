# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import tempfile
from app_runtime import db


def BenchmarkTest04723():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(comment_value)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
