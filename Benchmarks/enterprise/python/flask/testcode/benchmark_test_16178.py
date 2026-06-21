# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest16178():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    os.system('echo ' + str(forwarded_ip))
    return jsonify({"result": "success"})
