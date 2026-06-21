# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest71691():
    ua_value = request.headers.get('User-Agent', '')
    pending = list(str(ua_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
