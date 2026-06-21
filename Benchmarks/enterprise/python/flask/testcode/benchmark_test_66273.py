# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest66273():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
