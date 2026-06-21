# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest06862():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value}'
    os.remove(str(data))
    return jsonify({"result": "success"})
