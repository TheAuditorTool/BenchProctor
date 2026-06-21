# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09762():
    cookie_value = request.cookies.get('session_token', '')
    pending = list(str(cookie_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
