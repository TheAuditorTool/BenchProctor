# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07690():
    referer_value = request.headers.get('Referer', '')
    return jsonify({'error': 'An internal error occurred'}), 500
