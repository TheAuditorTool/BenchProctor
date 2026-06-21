# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest57161():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
