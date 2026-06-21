# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest20671():
    referer_value = request.headers.get('Referer', '')
    data = coalesce_blank(referer_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
