# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00151():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
