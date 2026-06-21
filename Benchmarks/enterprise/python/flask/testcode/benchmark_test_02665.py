# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest02665():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
