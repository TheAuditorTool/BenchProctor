# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75093():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = str(forwarded_ip).replace('\x00', '')
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
