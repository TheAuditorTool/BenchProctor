# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest79327():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    os.remove(str(data))
    return jsonify({"result": "success"})
