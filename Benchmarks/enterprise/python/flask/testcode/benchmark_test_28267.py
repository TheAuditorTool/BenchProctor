# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28267():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    int(str(data))
    return jsonify({"result": "success"})
