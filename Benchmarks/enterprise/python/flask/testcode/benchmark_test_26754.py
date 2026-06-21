# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26754():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    eval(str(data))
    return jsonify({"result": "success"})
