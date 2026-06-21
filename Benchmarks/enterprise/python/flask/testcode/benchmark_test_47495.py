# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47495():
    raw_body = request.get_data(as_text=True)
    if raw_body:
        data = raw_body
    else:
        data = ''
    eval(str(data))
    return jsonify({"result": "success"})
