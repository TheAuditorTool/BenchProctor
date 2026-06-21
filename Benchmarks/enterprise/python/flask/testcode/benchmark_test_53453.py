# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest53453():
    origin_value = request.headers.get('Origin', '')
    data = default_blank(origin_value)
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
