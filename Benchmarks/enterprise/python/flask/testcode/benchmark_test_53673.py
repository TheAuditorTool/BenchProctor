# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53673():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % str(forwarded_ip)
    int(str(data))
    return jsonify({"result": "success"})
