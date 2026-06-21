# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest63731():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
