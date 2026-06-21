# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34514():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    eval(str(data))
    return jsonify({"result": "success"})
