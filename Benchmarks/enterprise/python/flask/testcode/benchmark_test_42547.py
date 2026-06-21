# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def coalesce_blank(value):
    return value or ''

def BenchmarkTest42547():
    header_value = request.headers.get('X-Custom-Header', '')
    data = coalesce_blank(header_value)
    processed = data[:64]
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return jsonify({'validated': str(processed)}), 200
    return jsonify({"result": "success"})
