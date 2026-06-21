# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72592():
    raw_body = request.get_data(as_text=True)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(raw_body)}
