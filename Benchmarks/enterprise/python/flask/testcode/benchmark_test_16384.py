# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import importlib


request_state: dict[str, str] = {}

def BenchmarkTest16384():
    referer_value = request.headers.get('Referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        importlib.import_module(str(data))
    return jsonify({"result": "success"})
