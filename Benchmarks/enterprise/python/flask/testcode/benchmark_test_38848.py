# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest38848():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    os.remove(str(data))
    return jsonify({"result": "success"})
