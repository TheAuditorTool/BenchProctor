# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74163():
    raw_body = request.get_data(as_text=True)
    prefix = ''
    data = prefix + str(raw_body)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
