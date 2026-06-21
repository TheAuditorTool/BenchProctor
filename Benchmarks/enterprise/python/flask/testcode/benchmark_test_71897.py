# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest71897():
    raw_body = request.get_data(as_text=True)
    reader = make_reader(raw_body)
    data = reader()
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
