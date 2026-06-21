# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49965():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    return jsonify({'error': 'An internal error occurred'}), 500
