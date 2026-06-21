# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest43678():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
