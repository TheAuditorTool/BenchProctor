# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
import importlib


def BenchmarkTest73068():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
