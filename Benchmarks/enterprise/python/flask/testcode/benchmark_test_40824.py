# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest40824():
    host_value = request.headers.get('Host', '')
    data = '%s' % (host_value,)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
