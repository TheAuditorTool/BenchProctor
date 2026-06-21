# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29891():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = str(forwarded_ip).replace('\x00', '')
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
