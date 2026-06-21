# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46364():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if not str(forwarded_ip).isdigit():
        raise ValueError('invalid input: ' + str(forwarded_ip))
    return jsonify({"result": "success"})
