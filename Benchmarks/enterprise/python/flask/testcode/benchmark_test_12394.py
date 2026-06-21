# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12394():
    raw_body = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    int(str(data))
    return jsonify({"result": "success"})
