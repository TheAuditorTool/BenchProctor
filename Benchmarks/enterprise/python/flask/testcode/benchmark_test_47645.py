# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47645():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
