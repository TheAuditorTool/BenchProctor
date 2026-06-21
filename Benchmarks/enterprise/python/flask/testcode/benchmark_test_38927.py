# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest38927():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
