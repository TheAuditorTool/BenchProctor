# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest16249():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '{}'.format(header_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
