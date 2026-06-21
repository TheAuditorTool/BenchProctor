# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest09411():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value:.200s}'
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
