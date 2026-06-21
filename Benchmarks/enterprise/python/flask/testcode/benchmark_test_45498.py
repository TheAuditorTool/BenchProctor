# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45498():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    return jsonify({'error': 'An internal error occurred'}), 500
