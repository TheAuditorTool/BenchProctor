# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11293():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
