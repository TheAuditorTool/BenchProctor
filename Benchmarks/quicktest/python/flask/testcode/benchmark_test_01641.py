# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest01641():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
