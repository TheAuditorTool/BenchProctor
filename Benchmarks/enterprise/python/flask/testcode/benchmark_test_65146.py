# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65146():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
