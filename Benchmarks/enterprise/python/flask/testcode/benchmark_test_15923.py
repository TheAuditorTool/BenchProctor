# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest15923():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    return jsonify({'error': 'An internal error occurred'}), 500
