# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42143():
    field_value = request.form.get('field', '')
    data = '%s' % (field_value,)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
