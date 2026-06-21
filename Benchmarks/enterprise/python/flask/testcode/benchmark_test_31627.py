# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest31627():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = coalesce_blank(comment_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return jsonify({"result": "success"})
