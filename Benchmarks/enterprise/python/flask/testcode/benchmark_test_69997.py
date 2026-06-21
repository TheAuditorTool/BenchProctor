# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69997():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
