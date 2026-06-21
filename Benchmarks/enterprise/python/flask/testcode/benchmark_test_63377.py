# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import tempfile
from app_runtime import db


def BenchmarkTest63377():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if comment_value:
        data = comment_value
    else:
        data = ''
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
