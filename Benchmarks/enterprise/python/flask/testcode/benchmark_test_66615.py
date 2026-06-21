# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def ensure_str(value):
    return str(value)

def BenchmarkTest66615():
    referer_value = request.headers.get('Referer', '')
    data = ensure_str(referer_value)
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
