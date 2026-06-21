# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54610():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
