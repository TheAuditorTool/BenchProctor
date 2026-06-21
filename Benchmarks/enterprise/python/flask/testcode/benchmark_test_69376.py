# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time
import ast


def BenchmarkTest69376():
    xml_value = request.get_data(as_text=True)
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    if time.time() > 1000000000:
        requests.get(str(data))
    return jsonify({"result": "success"})
