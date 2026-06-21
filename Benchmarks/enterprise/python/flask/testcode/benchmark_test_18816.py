# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
from app_runtime import db, auth_check


def BenchmarkTest18816():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % str(comment_value)
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return jsonify({"result": "success"})
