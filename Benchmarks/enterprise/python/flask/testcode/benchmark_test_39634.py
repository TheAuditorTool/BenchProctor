# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest39634():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '{}'.format(header_value)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
