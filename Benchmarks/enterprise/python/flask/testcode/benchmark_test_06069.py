# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06069():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
