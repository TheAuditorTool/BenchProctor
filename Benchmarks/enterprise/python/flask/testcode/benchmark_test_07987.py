# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07987():
    header_value = request.headers.get('X-Custom-Header', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
