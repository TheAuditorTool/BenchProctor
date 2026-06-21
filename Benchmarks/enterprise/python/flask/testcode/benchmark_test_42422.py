# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest42422():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
