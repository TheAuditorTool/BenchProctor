# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest32071():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    importlib.import_module(str(forwarded_ip))
    return jsonify({"result": "success"})
