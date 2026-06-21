# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib
import sys
from app_runtime import db


def BenchmarkTest55131():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = (lambda v: v.strip())(db_value)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
