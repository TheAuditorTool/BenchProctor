# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32643():
    multipart_value = request.form.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
