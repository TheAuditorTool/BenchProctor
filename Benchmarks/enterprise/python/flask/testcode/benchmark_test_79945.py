# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest79945():
    referer_value = request.headers.get('Referer', '')
    data = coalesce_blank(referer_value)
    return jsonify({'error': 'An internal error occurred'}), 500
