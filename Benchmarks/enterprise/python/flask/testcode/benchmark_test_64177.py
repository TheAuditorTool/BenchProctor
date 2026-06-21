# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest64177():
    host_value = request.headers.get('Host', '')
    data = coalesce_blank(host_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
