# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify
from app_runtime import db


def BenchmarkTest29391():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if comment_value:
        data = comment_value
    else:
        data = ''
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
