# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest37144():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    os.remove(str(data))
    return jsonify({"result": "success"})
