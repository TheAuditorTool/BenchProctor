# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
from app_runtime import db


def BenchmarkTest55316():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % str(comment_value)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
