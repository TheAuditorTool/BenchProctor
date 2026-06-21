# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest51602():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
