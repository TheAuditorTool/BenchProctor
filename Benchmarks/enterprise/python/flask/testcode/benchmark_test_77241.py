# SPDX-License-Identifier: Apache-2.0
import secrets
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest77241():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
