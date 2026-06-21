# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


def BenchmarkTest18605():
    xml_value = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
