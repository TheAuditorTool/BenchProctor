# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest34836():
    ua_value = request.headers.get('User-Agent', '')
    pending = list(str(ua_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
