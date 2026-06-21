# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08802():
    raw_body = request.get_data(as_text=True)
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
