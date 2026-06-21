# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest03141():
    cookie_value = request.cookies.get('session_token', '')
    data = '{}'.format(cookie_value)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
