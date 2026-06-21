# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


def BenchmarkTest70251():
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
