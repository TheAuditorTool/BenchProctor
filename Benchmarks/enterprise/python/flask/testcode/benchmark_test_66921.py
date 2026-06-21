# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest66921():
    field_value = request.form.get('field', '')
    data = '%s' % (field_value,)
    eval(str(data))
    return jsonify({"result": "success"})
