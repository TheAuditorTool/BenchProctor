# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest61142():
    header_value = request.headers.get('X-Custom-Header', '')
    os.remove(str(header_value))
    return jsonify({"result": "success"})
