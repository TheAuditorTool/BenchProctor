# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47912():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    return jsonify({'error': 'An internal error occurred'}), 500
