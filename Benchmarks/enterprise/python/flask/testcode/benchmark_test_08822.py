# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest08822():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    os.remove(str(data))
    return jsonify({"result": "success"})
