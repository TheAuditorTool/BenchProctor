# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43452():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    trusted_claim = str(json_value)
    return jsonify({'trusted': trusted_claim}), 200
