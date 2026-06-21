# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import pickle
from app_runtime import db


def BenchmarkTest43207():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = str(comment_value).replace('\x00', '')
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
