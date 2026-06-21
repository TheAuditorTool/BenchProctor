# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session


def to_text(value):
    return str(value).strip()

def BenchmarkTest69620():
    referer_value = request.headers.get('Referer', '')
    data = to_text(referer_value)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
