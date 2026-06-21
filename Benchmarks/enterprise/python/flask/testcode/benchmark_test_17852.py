# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest17852():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
