# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest00141():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value}'
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
