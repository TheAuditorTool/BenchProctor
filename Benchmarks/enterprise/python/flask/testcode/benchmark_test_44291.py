# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest44291():
    referer_value = request.headers.get('Referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
