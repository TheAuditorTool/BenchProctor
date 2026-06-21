# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56042():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    return jsonify({'error': 'An internal error occurred'}), 500
