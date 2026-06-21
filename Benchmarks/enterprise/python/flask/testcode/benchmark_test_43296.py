# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest43296():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
