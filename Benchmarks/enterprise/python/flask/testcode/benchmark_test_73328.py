# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest73328():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
