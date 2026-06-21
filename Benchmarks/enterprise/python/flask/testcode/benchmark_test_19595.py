# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import importlib
import sys


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest19595():
    xml_value = request.get_data(as_text=True)
    data = default_blank(xml_value)
    if os.environ.get("APP_ENV", "production") != "test":
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
