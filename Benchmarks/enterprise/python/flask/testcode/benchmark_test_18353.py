# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18353():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
