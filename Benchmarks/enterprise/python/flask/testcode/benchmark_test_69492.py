# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest69492():
    host_value = request.headers.get('Host', '')
    os.remove(str(host_value))
    return jsonify({"result": "success"})
