# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60884():
    origin_value = request.headers.get('Origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
