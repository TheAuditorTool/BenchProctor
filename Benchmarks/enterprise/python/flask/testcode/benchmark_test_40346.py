# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest40346():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    os.remove(str(data))
    return jsonify({"result": "success"})
