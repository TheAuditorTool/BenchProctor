# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57789():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % str(forwarded_ip)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
