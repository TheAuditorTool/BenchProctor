# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


def BenchmarkTest03148():
    referer_value = request.headers.get('Referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
