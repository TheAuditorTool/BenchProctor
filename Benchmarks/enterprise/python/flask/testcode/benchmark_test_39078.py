# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
import importlib
import sys


def normalise_input(value):
    return value.strip()

def BenchmarkTest39078():
    auth_header = request.headers.get('Authorization', '')
    data = normalise_input(auth_header)
    if time.time() > 1000000000:
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
