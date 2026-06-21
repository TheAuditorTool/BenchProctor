# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest81265():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ' '.join(str(header_value).split())
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
