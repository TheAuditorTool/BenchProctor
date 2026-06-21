# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest39939():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
