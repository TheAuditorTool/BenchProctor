# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify
from app_runtime import db


def BenchmarkTest08416():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
