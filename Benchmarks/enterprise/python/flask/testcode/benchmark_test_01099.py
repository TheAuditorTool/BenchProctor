# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest01099():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = coalesce_blank(comment_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200
