# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest71642():
    header_value = request.headers.get('X-Custom-Header', '')
    data = to_text(header_value)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
