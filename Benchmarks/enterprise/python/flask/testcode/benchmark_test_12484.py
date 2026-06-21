# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest12484():
    host_value = request.headers.get('Host', '')
    data = relay_value(host_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
