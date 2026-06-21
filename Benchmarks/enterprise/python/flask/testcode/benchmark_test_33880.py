# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
import importlib
import sys
from types import SimpleNamespace


def BenchmarkTest33880():
    xml_value = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
