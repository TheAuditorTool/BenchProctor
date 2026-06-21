# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest67688():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
