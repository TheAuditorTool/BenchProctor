# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02412():
    host_value = request.headers.get('Host', '')
    data = '%s' % (host_value,)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
