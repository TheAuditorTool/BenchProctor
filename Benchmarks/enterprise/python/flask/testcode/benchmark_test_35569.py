# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest35569():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % str(ua_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
