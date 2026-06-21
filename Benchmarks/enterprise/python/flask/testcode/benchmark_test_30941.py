# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


def BenchmarkTest30941():
    user_id = request.args.get('id', '')
    sys.path.insert(0, str(user_id))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
