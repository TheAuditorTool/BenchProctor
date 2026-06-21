# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


def BenchmarkTest62593():
    cookie_value = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
