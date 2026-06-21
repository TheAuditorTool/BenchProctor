# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38369():
    referer_value = request.headers.get('Referer', '')
    parts = []
    for token in str(referer_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
