# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest12754():
    host_value = request.headers.get('Host', '')
    data = '%s' % str(host_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
