# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27748():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    eval(str(data))
    return jsonify({"result": "success"})
