# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest28339():
    xml_value = request.get_data(as_text=True)
    data = '%s' % str(xml_value)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
