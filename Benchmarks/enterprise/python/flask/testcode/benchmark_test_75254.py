# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75254():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
