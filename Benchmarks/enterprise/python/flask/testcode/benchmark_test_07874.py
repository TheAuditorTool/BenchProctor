# SPDX-License-Identifier: Apache-2.0
import base64
from flask import jsonify
import pickle
from app_runtime import db


def BenchmarkTest07874():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
