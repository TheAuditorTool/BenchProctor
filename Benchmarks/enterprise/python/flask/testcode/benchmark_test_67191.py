# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest67191():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
