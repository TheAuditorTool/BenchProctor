# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest59543():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(comment_value))
    return jsonify({"result": "success"})
