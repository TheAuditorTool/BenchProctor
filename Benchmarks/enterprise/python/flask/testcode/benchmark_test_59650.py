# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59650():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    eval(str(data))
    return jsonify({"result": "success"})
