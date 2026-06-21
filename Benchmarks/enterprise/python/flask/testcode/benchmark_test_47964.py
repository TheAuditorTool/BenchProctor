# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest47964():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value}'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
