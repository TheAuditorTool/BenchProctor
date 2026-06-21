# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79416():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
