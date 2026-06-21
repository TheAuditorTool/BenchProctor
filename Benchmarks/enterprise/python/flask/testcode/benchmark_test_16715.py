# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16715():
    multipart_value = request.form.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
