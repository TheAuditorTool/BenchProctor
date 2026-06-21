# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
import importlib


def BenchmarkTest30365():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
