# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest46635():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % str(referer_value)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
