# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
import importlib


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest11819():
    upload_name = request.files['upload'].filename
    data = default_blank(upload_name)
    if time.time() > 1000000000:
        importlib.import_module(str(data))
    return jsonify({"result": "success"})
