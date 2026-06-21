# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest00489():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
