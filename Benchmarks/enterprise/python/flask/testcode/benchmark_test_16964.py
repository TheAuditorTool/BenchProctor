# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16964():
    multipart_value = request.form.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
