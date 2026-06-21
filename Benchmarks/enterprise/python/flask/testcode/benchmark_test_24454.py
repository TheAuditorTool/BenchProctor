# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import importlib
import sys


def BenchmarkTest24454():
    user_id = request.args.get('id', '')
    try:
        data = json.loads(user_id).get('value', user_id)
    except (json.JSONDecodeError, AttributeError):
        data = user_id
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
