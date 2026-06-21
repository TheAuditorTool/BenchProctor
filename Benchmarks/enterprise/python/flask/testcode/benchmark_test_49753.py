# SPDX-License-Identifier: Apache-2.0
import html
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest49753():
    host_value = request.headers.get('Host', '')
    data = coalesce_blank(host_value)
    processed = str(data).replace("<script", "")
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
