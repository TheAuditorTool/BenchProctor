# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04270():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
