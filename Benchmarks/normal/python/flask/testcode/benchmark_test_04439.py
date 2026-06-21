# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import pickle
from app_runtime import db


def BenchmarkTest04439():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    pickle.loads(db_value.encode('latin-1'))
    return jsonify({"result": "success"})
