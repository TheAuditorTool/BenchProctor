# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest45839():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(comment_value))
    return jsonify({"result": "success"})
