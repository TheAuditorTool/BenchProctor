# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19017():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % str(forwarded_ip)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
