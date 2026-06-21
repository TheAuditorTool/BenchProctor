# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib
from app_runtime import db


def BenchmarkTest63860():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(db_value)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
