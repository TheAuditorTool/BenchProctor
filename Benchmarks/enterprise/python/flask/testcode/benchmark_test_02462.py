# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
import importlib
import sys


def BenchmarkTest02462():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
