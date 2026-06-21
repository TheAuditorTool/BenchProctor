# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14644():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
