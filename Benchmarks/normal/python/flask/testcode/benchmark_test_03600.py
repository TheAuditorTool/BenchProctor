# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest03600():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % (ua_value,)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
