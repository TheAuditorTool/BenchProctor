# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07012():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    eval(str(data))
    return jsonify({"result": "success"})
