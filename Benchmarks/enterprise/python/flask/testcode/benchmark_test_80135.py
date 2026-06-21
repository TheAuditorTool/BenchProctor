# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80135():
    host_value = request.headers.get('Host', '')
    data = '%s' % str(host_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
