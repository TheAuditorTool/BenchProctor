# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42064():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
