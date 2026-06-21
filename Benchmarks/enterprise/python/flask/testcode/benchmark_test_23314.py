# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest23314():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body}'
    int(str(data))
    return jsonify({"result": "success"})
