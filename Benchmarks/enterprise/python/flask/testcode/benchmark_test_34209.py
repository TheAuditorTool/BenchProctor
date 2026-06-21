# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34209():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
