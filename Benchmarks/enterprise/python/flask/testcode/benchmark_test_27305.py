# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27305():
    ua_value = request.headers.get('User-Agent', '')
    pending = list(str(ua_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return jsonify({'error': 'An internal error occurred'}), 500
