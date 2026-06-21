# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest66189():
    referer_value = request.headers.get('Referer', '')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
