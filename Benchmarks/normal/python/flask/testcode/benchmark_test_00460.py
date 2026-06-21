# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00460():
    raw_body = request.get_data(as_text=True)
    prefix = ''
    data = prefix + str(raw_body)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
