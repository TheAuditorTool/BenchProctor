# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25581():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = str(forwarded_ip).replace('\x00', '')
    eval(str(data))
    return jsonify({"result": "success"})
