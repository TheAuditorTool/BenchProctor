# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time
import ast


def BenchmarkTest14125():
    raw_body = request.get_data(as_text=True)
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    if time.time() > 1000000000:
        requests.get(str(data))
    return jsonify({"result": "success"})
