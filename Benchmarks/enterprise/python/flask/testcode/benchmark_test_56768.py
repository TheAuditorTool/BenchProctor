# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest56768():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
