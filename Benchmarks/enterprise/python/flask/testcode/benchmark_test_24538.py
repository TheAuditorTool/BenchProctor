# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest24538():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = relay_value(comment_value)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
