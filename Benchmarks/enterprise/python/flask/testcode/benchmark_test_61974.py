# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest61974():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % str(referer_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
