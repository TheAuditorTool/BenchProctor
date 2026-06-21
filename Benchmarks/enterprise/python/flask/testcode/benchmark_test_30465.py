# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest30465():
    host_value = request.headers.get('Host', '')
    data = ensure_str(host_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
