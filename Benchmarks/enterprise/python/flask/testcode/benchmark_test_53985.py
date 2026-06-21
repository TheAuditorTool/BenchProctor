# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53985():
    field_value = request.form.get('field', '')
    raise RuntimeError('processing failed: ' + str(field_value))
    return jsonify({"result": "success"})
