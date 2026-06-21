# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest70032():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
