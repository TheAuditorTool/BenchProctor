# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from flask import session


def BenchmarkTest32863():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
