# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest47460():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
