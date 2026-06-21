# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest71854():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
