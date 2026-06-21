# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest43939():
    host_value = request.headers.get('Host', '')
    data = '{}'.format(host_value)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
