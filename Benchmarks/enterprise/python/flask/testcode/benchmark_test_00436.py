# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest00436():
    header_value = request.headers.get('X-Custom-Header', '')
    data = relay_value(header_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
