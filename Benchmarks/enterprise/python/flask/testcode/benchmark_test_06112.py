# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06112():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
