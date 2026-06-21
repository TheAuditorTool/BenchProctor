# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest28992():
    raw_body = request.get_data(as_text=True)
    data = normalise_input(raw_body)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
