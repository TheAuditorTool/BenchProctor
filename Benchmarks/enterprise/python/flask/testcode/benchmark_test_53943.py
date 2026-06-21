# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53943():
    raw_body = request.get_data(as_text=True)
    data = '{}'.format(raw_body)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
