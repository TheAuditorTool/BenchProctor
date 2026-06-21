# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62540():
    raw_body = request.get_data(as_text=True)
    data, _sep, _rest = str(raw_body).partition('\x00')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
