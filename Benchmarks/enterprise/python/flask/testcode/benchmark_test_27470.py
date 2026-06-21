# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
import os
from app_runtime import db


def BenchmarkTest27470():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % (comment_value,)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
