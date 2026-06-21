# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest63348():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % str(comment_value)
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})
