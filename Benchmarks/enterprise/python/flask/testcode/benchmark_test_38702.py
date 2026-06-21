# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest38702():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
