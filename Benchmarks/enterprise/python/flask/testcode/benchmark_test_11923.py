# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib
from app_runtime import db


def BenchmarkTest11923():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    importlib.import_module(str(db_value))
    return jsonify({"result": "success"})
