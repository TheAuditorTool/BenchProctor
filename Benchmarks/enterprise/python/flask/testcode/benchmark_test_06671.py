# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest06671():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
