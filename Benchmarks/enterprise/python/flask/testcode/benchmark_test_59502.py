# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest59502():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = str(comment_value).replace('\x00', '')
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return jsonify({'secret': str(secret)}), 200
