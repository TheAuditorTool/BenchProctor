# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest49270():
    referer_value = request.headers.get('Referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
