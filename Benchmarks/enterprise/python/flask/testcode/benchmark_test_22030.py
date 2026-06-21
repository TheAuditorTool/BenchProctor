# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22030():
    auth_header = request.headers.get('Authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
