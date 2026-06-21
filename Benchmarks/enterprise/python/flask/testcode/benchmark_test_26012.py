# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest26012():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    os.remove(str(forwarded_ip))
    return jsonify({"result": "success"})
