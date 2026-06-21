# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12066():
    raw_body = request.get_data(as_text=True)
    return jsonify({'error': str(raw_body), 'stack': repr(locals())}), 500
