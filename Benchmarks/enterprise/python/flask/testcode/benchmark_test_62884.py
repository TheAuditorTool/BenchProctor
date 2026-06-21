# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62884():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
