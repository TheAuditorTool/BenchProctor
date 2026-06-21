# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14560():
    multipart_value = request.form.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
