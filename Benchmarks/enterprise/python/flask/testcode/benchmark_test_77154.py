# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77154():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip}'
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
