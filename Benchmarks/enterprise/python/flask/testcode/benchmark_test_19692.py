# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19692():
    raw_body = request.get_data(as_text=True)
    prefix = ''
    data = prefix + str(raw_body)
    int(str(data))
    return jsonify({"result": "success"})
