# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session


def BenchmarkTest65283():
    host_value = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
