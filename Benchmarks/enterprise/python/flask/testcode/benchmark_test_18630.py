# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest18630():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip}'
    os.remove(str(data))
    return jsonify({"result": "success"})
