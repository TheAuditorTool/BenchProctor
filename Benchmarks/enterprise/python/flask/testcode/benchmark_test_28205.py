# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest28205():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
