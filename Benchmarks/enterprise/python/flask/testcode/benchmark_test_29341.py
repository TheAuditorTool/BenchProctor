# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest29341():
    header_value = request.headers.get('X-Custom-Header', '')
    random.seed(int(header_value) if str(header_value).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
