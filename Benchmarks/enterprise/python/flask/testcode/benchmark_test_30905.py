# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import json
import importlib
import sys
from app_runtime import db


def BenchmarkTest30905():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
