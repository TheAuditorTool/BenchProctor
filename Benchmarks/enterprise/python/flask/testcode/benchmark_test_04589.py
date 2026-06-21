# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
import importlib
import sys


def BenchmarkTest04589():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
