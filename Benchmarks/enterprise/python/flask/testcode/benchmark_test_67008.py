# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib
import sys
from app_runtime import db


def BenchmarkTest67008():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '{}'.format(comment_value)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
