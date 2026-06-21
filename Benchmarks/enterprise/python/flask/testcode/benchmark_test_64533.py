# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64533():
    field_value = request.form.get('field', '')
    data = '{}'.format(field_value)
    exec(str(data))
    return jsonify({"result": "success"})
