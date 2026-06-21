# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22039():
    field_value = request.form.get('field', '')
    data = '%s' % (field_value,)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
