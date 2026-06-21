# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest40287():
    referer_value = request.headers.get('Referer', '')
    reader = make_reader(referer_value)
    data = reader()
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
