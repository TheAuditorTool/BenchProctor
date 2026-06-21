# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib
import sys
from app_runtime import db


def BenchmarkTest56417():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data, _sep, _rest = str(db_value).partition('\x00')
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
