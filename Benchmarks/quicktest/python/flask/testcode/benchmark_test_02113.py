# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest02113():
    host_value = request.headers.get('Host', '')
    data = coalesce_blank(host_value)
    return jsonify({'error': 'An internal error occurred'}), 500
