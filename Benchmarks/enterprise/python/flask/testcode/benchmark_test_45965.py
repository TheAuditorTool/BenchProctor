# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45965():
    origin_value = request.headers.get('Origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
