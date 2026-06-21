# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19911():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
