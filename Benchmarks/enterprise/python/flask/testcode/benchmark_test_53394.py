# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53394():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
