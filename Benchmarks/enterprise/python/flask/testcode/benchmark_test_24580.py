# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24580():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
