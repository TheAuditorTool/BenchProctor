# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest11563():
    raw_body = request.get_data(as_text=True)
    data = coalesce_blank(raw_body)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return str(processed), 200, {'Content-Type': 'text/html'}
