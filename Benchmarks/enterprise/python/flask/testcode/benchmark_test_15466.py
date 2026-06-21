# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15466():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    parts = str(json_value).split(',')
    data = ','.join(parts)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
