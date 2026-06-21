# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06426():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
