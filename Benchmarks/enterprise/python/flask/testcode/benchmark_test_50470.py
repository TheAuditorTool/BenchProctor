# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50470():
    field_value = request.form.get('field', '')
    data = f'{field_value}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
