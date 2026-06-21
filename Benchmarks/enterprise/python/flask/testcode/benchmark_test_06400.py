# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06400():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(forwarded_ip) + ',data\n')
    return jsonify({"result": "success"})
