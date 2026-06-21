# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest78464():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
