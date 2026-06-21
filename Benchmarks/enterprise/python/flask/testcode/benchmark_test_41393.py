# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import pickle
from app_runtime import db


def BenchmarkTest41393():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if comment_value:
        data = comment_value
    else:
        data = ''
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
