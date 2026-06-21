# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69801():
    header_value = request.headers.get('X-Custom-Header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
