# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest00670():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
