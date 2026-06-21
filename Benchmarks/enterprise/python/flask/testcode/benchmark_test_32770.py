# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest32770():
    host_value = request.headers.get('Host', '')
    data = '{}'.format(host_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
