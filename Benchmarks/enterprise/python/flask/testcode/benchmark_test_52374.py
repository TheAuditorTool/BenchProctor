# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db, auth_check


def BenchmarkTest52374():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value:.200s}'
    auth_check('user', data)
    return jsonify({"result": "success"})
