# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest29983():
    host_value = request.headers.get('Host', '')
    os.system('echo ' + str(host_value))
    return jsonify({"result": "success"})
